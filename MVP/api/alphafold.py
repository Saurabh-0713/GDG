from fastapi import APIRouter, UploadFile, File
import subprocess
import os

router = APIRouter()

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/predict_structure/")
async def predict_structure(file: UploadFile = File(...)):
    """Runs AlphaFold2 to predict a protein's 3D structure from a FASTA file."""
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    command = f"bash run_alphafold.sh {file_path}"
    subprocess.run(command, shell=True)

    return {"message": "Protein structure prediction started", "file": file.filename}
