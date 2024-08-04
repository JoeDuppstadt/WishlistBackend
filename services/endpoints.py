from fastapi import FastAPI

import DBManager

app = FastAPI()


# fastapi dev /Users/josephduppstadt/Documents/WishlistBackend/services/endpoints.py
@app.get("/getAllItems")
async def read_root():
    print('here')
    conn = connectDB()
    return {'here'}
