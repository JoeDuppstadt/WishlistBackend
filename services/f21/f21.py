import json
import requests
import re
from classes.f21.f21Class import Root
from classes.f21.f21DetailsClass import RootDetails
from helpers.fileio import readItemsOutput, saveDetailsOutput, readDetailsOutput
import pymysql
from dotenv import load_dotenv
import os
def getProductDetails(PID):
    url = "https://apidojo-forever21-v1.p.rapidapi.com/products/v2/detail"
    querystring = {"productId": PID}
    headers = {
        "X-RapidAPI-Key": "c24a2be811msh82c950a50f6cd83p1409a8jsn127d7ba7941a",
        "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return str(response.json())


def getProducts():
    url = "https://apidojo-forever21-v1.p.rapidapi.com/products/search"
    querystring = {"query": "jackets", "rows": "3", "start": "0", "color_groups": "black"}
    headers = {
        "X-RapidAPI-Key": "c24a2be811msh82c950a50f6cd83p1409a8jsn127d7ba7941a",
        "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return str(response.json())


def removeHTMLTags(textWithHTML):
    reg_str = '<div class="d_content">(.*?)<p>'
    str = re.findall(reg_str, textWithHTML)
    clean = re.compile('<.*?>')
    return re.sub(clean, '', str[0])


def orderImages(imageList):
    ordered_list = []
    for image in imageList:
        if image not in ordered_list:
            ordered_list.append(image)
    return ordered_list


def connectDB():
    load_dotenv()
    user = os.getenv("WishlistUser")
    password = os.getenv("WishlistDBPass")
    host = os.getenv("WishlistDBHost")
    print(password)

    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db='Wishlist',
    )
    return conn

conn = connectDB()
# Example Usage
jsonstring = json.loads(readItemsOutput())
root = Root.from_dict(jsonstring)

PID = root.response.docs[0].pid

title = root.response.docs[0].title
price = root.response.docs[0].sale_price
url = root.response.docs[0].url
brand = 'Forever21'

jsonDetailsString = json.loads(readDetailsOutput())
rootDetails = RootDetails.from_dict(jsonDetailsString)

description = removeHTMLTags(rootDetails.product.Description)
image1url = rootDetails.product.DefaultProductImage

image1url = None
image2url = None
image3url = None
image4url = None
image5url = None
image6url = None

product_images = orderImages(rootDetails.product.Variants[0].ProductImages[0])
try:
    if product_images[0] is not None:
        image1url = product_images[0]
    print(image1url)
except:
    print("No Image 1")
try:
    if product_images[1] is not None:
        image2url = product_images[1]
    print(image2url)
except:
    print("No Image 2")
try:
    if product_images[2] is not None:
        image3url = product_images[3]
    print(image3url)
except:
    print("No Image 3")
try:
    if product_images[3] is not None:
        image4url = product_images[4]
    print(image4url)
except:
    print("No Image 4")
try:
    if product_images[4] is not None:
        image5url = product_images[5]
    print(image5url)
except:
    print("No Image 5")
try:
    if product_images[5] is not None:
        image6url = product_images[6]
    print(image6url)
except:
    print("No Image 6")



cur = conn.cursor()
cur.execute("select @@version")
output = cur.fetchall()
print(output)