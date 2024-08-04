
from services.DBManager import connectDB, returnAllItems
conn = connectDB()

print(returnAllItems(conn))
