import datetime
import time
import pymysql
from dotenv import load_dotenv
import os


def connectDB():
    load_dotenv()
    user = os.getenv("WishlistUser")
    password = os.getenv("WishlistDBPass")
    host = os.getenv("WishlistDBHost")

    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db='Wishlist',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn


def insertIntoItemMaster(conn, DBPKEY, title, description, brand, contentRating, url):
    time.sleep(0.1)
    cur = conn.cursor()
    cur.execute(
        'insert into Wishlist.ItemMaster(PID, Title, Description, Brand, ContentRating, URL, Created) values(%s,%s,%s,%s,%s,%s,%s);',
        (DBPKEY, title, description, brand, contentRating, url, datetime.datetime.now(),))
    conn.commit()


def insertIntoItemAssets(conn, DBPKEY, image1, image2, image3, image4, image5, image6):
    time.sleep(0.1)
    cur = conn.cursor()
    cur.execute(
        'insert into Wishlist.ItemAssets(PID, ImageURL1, ImageURL2, ImageURL3, ImageURL4, ImageURL5, ImageURL6) values(%s,%s,%s,%s,%s,%s,%s);',
        (DBPKEY, image1, image2, image3, image4, image5, image6,))
    conn.commit()


def insertIntoItemPricing(conn, DBPKEY, price):
    time.sleep(0.1)
    cur = conn.cursor()
    cur.execute(
        'insert into Wishlist.ItemPricing(PID,  Price) values(%s,%s);',
        (DBPKEY, price,))
    conn.commit()


def searchBeforeCreate(conn, DBPKEY):
    time.sleep(0.1)
    cur = conn.cursor()
    cur.execute("select count(*) as cnt from ItemMaster where PID = '%s'" % DBPKEY)
    time.sleep(0.25)
    result = cur.fetchone()
    if result['cnt'] == 1:
        return True
    return False


def returnAllItems(conn):
    cur = conn.cursor()
    cur.execute("select * from Wishlist.ItemMaster im inner  join Wishlist.ItemAssets ia on im.PID = ia.PID inner "
                "join Wishlist.ItemPricing ip on im.PID = ip.PID ")
    result = cur.fetchall()
    print(result)


def checkStatus(conn):
    cur = conn.cursor()
    cur.execute("select im.PID, ImageURL1 from Wishlist.ItemMaster im inner join Wishlist.ItemAssets ia on im.PID = ia.PID;")
    result = cur.fetchall()
    return result


def setStatusCode(conn, PID, STATUSCODE):
    cur = conn.cursor()
    cur.execute(
        'UPDATE Wishlist.ItemMaster SET StatusCode = %s WHERE PID = %s;',
        (STATUSCODE, PID))
    conn.commit()
