from fastapi import APIRouter, UploadFile, File
from MVP.gdrive_auth import authenticate_gdrive


router = APIRouter()

drive = authenticate_gdrive()

@router.post("/upload/")
async def upload_to_gdrive(file: UploadFile = File(...)):
    """Uploads results to Google Drive."""
    file_content = await file.read()

    gfile = drive.CreateFile({'title': file.filename})
    gfile.SetContentString(file_content.decode('utf-8'))
    gfile.Upload()

    return {"message": "File uploaded successfully", "filename": file.filename}
