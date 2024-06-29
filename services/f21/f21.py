import json
import time
import requests
import re
from classes.f21.f21Class import Root
from classes.f21.f21DetailsClass import RootDetails
from helpers.fileio import readItemsOutput, saveItemsOutput
from services.DBManager import connectDB, insertIntoItemMaster, insertIntoItemAssets, insertIntoItemPricing


def getProductDetails(PID):
    url = "https://apidojo-forever21-v1.p.rapidapi.com/products/v2/detail"
    querystring = {"productId": PID}
    headers = {
        "X-RapidAPI-Key": "c24a2be811msh82c950a50f6cd83p1409a8jsn127d7ba7941a",
        "X-RapidAPI-Host": "apidojo-forever21-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return str(response.text)


def getProducts():
    url = "https://apidojo-forever21-v1.p.rapidapi.com/products/search"
    querystring = {"query": "jackets", "rows": "1", "start": "0", "color_groups": "black"}
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





# saveItemsOutput(getProducts())

jsonstring = json.loads(readItemsOutput())
root = Root.from_dict(jsonstring)

conn = connectDB()
title = root.response.docs[0].title
price = root.response.docs[0].sale_price
url = root.response.docs[0].url
brand = 'Forever21'
contentRating = None
PID = root.response.docs[0].pid
DBPKEY = root.response.docs[0].pid + '||' + brand
print(title)
print(price)
print(PID)
print(url)
time.sleep(0.1)
jsonDetailsString = json.loads(getProductDetails(PID))
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
time.sleep(1)
insertIntoItemMaster(conn, DBPKEY, title, description, brand, contentRating, url)
insertIntoItemAssets(conn, DBPKEY, image1url, image2url, image3url, image4url, image5url, image6url)
insertIntoItemPricing(conn, DBPKEY, price)