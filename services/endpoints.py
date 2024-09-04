from fastapi import FastAPI, Depends, HTTPException
import DBManager
from fastapi.security import APIKeyHeader
import os
from dotenv import load_dotenv
import logging
import logging.config

app = FastAPI()

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logging.log',
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

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
    logging.info('Attempting to connect to DB')
    conn = DBManager.connectDB()
    logging.info('Connected to DB')
    data = DBManager.returnAllActiveItems(conn)
    logging.info('Returned all active items')
    return [
        data
    ]
