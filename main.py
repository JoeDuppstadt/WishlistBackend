
from services.DBManager import connectDB,  returnAllActiveItems

conn = connectDB()

print(returnAllActiveItems(conn))
