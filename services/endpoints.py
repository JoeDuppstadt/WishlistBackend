from fastapi import FastAPI, Depends, HTTPException
import DBManager
from fastapi.security import APIKeyHeader
import os
from dotenv import load_dotenv

app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-KEY")
load_dotenv()
API_KEY = os.getenv("API_KEY")
def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    return api_key


# http://127.0.0.1:8000/getAllItems
# fastapi dev /Users/josephduppstadt/Documents/WishlistBackend/services/endpoints.py
@app.get("/getAllItems")
async def read_root(api_key: str = Depends(verify_api_key)):
    conn = DBManager.connectDB()
    data = DBManager.returnAllActiveItems(conn)
    return [
        data
    ]
