from fastapi import APIRouter, UploadFile, File
import subprocess
import os

router = APIRouter()

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/optimize_docking/")
async def optimize_docking(protein_file: UploadFile = File(...), ligand_file: UploadFile = File(...)):
    """Optimizes molecular docking using DiffDock."""
    protein_path = os.path.join(UPLOAD_DIR, protein_file.filename)
    ligand_path = os.path.join(UPLOAD_DIR, ligand_file.filename)

    with open(protein_path, "wb") as f:
        f.write(await protein_file.read())
    with open(ligand_path, "wb") as f:
        f.write(await ligand_file.read())

    command = f"bash run_diffdock.sh {protein_path} {ligand_path}"
    subprocess.run(command, shell=True)

    return {"message": "Molecular docking started", "protein": protein_file.filename, "ligand": ligand_file.filename}
