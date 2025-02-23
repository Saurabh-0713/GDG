from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.post("/generate_molecule/")
async def generate_molecule(smiles: str):
    """Generates small molecules using MolMIM."""
    command = f"python run_molmim.py --smiles '{smiles}'"
    subprocess.run(command, shell=True)

    return {"message": "Molecule generation started", "input": smiles}
