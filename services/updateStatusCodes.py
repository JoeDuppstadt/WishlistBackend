import requests
from services.DBManager import connectDB, checkStatus, setStatusCode


def getStatusCode(url):
    # create header to mimic user
    head = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'refere': 'https://google.com',
        'cookie': """your cookie value ( you can get that from your web page) """
    }

    response = requests.get(url, headers=head)
    return response.status_code


conn = connectDB()  # create database connection

URLS = checkStatus(conn)  # return URLS

length = len(URLS)  # create length variable so we can iterate over a list

for i in range(length):  # iterate over the of ids
    statusCode = None
    pid = (URLS[i].get('PID'))  # grab the pid so set status
    url1 = (URLS[i].get('ImageURL1'))  # grab url to test
    url2 = (URLS[i].get('ImageURL2'))  # grab url to test
    url3 = (URLS[i].get('ImageURL3'))  # grab url to test
    print(pid)
    print(url1)

    url1StatusCode = getStatusCode(url1)
    url2StatusCode = getStatusCode(url2)
    url3StatusCode = getStatusCode(url3)
    print(url1StatusCode)
    print(url2StatusCode)
    print(url3StatusCode)
    statusCode = None

    if url1StatusCode == 200 and url2StatusCode == 200 and url3StatusCode == 200:
        statusCode = '200'
    else:
        statusCode = '404'

    print(statusCode)

    setStatusCode(conn, pid, statusCode)  # create a request to set the status in the itemmaster table
