from fastapi import FastAPI
from MVP.api import alphafold, molmim, oracle, diffdock, protein_design, gemini, storage


app = FastAPI(title="AI-Powered Drug Discovery API")

# Register API modules
app.include_router(alphafold.router)
app.include_router(molmim.router)
app.include_router(oracle.router)
app.include_router(diffdock.router)
app.include_router(protein_design.router)
app.include_router(gemini.router)
app.include_router(storage.router)

@app.get("/")
def home():
    return {"message": "AI-Powered Drug Discovery API is running!"}
