from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def authenticate_gdrive():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("gdrive_credentials.json")

    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile("gdrive_credentials.json")
    return GoogleDrive(gauth)
