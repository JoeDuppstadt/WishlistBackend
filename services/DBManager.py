import datetime
import time
import pymysql
from dotenv import load_dotenv
import os


def connectDB():
    try:
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
    except:
        raise Exception("Cannot connect to database")



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


def returnAllActiveItems(conn):
    cur = conn.cursor()
    cur.execute("select im.PID, im.Title, im.Description, im.Brand, im.URL, ia.ImageURL1, ia.ImageURL2, ia.ImageURL3, "
                "ia.ImageURL4, ia.ImageURL5, ia.ImageURL6, ia.ImageURL7, ip.Price, im.ContentRating from Wishlist.ItemMaster im inner "
                "join Wishlist.ItemAssets ia on im.PID = ia.PID inner join Wishlist.ItemPricing ip on im.PID = ip.PID "
                "where StatusCode = '200' order by RAND() limit 100")
    result = cur.fetchall()
    return result

def checkStatus(conn):
    cur = conn.cursor()
    cur.execute("select im.PID, ImageURL1, ImageURL2, ImageURL3 from Wishlist.ItemMaster im inner join Wishlist.ItemAssets ia on im.PID = ia.PID;")
    result = cur.fetchall()
    return result


def setStatusCode(conn, PID, STATUSCODE):
    cur = conn.cursor()
    cur.execute(
        'UPDATE Wishlist.ItemMaster SET StatusCode = %s WHERE PID = %s;',
        (STATUSCODE, PID))
    conn.commit()
