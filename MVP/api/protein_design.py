from fastapi import APIRouter, UploadFile, File
import subprocess
import os

router = APIRouter()

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/design_protein/")
async def design_protein(file: UploadFile = File(...)):
    """
    Accepts a protein sequence file and designs optimized protein binders.
    Uses RFDiffusion, ProteinMPNN, and AlphaFold-Multimer.
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Step 1: Run RFDiffusion (Optimizes protein conformations)
    command_rf = f"bash run_rfdiffusion.sh {file_path}"
    subprocess.run(command_rf, shell=True)

    # Step 2: Run ProteinMPNN (Designs stable protein sequences)
    command_mpnn = f"bash run_proteinmpnn.sh {file_path}"
    subprocess.run(command_mpnn, shell=True)

    # Step 3: Validate with AlphaFold-Multimer (Ensures stability)
    command_multimer = f"bash run_alphafold_multimer.sh {file_path}"
    subprocess.run(command_multimer, shell=True)

    return {"message": "Protein binder design started", "file": file.filename}
