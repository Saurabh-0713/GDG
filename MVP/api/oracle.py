import subprocess
from fastapi import APIRouter

router = APIRouter()

@router.post("/evaluate_molecule/")
async def evaluate_molecule(smiles: str):
    """Evaluates drug-likeness, ADMET properties, and binding affinity."""
    command = f"python run_oracle.py --smiles '{smiles}'"
    subprocess.run(command, shell=True)

    return {"message": "Molecule evaluation started", "input": smiles}
