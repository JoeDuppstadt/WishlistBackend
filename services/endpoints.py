from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
import DBManager

app = FastAPI()


class Item(BaseModel):
    pid: str
    title: str
    '''
    description: str
    brand: str
    url: str
    imageurl1: str
    imageurl2: str
    imageurl3: str
    imageurl4: str
    imageurl5: str
    imageurl6: str
    imageurl7: str
    price: str
'''

# http://127.0.0.1:8000/getAllItems
# fastapi dev /Users/josephduppstadt/Documents/WishlistBackend/services/endpoints.py
@app.get("/getAllItems")
async def read_root():
    conn = DBManager.connectDB()
    data = DBManager.returnAllActiveItems(conn)
    return [
        data
    ]
