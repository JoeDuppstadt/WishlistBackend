import json
import time

from fastapi import FastAPI

import DBManager

app = FastAPI()


# fastapi dev /Users/josephduppstadt/Documents/WishlistBackend/services/endpoints.py
@app.get("/getAllItems")
async def read_root():
    conn = DBManager.connectDB()
    data = DBManager.returnAllActiveItems(conn)
    json_data = json.dumps(data)
    return {json_data}
