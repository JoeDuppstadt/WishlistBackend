import time
from urllib.request import Request, urlopen

from services.DBManager import connectDB, checkStatus, setStatusCode

def get_page_content(url, head):
    req = Request(url, headers=head)
    return urlopen(req)


conn = connectDB()  # create database connection

URLS = checkStatus(conn)  # return URLS

length = len(URLS)

for i in range(length):
    statusCode = None
    pid = (URLS[i].get('PID'))
    url = (URLS[i].get('URL'))
    print(pid)
    print(url)
    head = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/99.0.4844.84 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'refere': 'https://example.com',
        'cookie': """your cookie value ( you can get that from your web page) """
    }

    try:
        data = (get_page_content(url, head)).read()
        time.sleep(0.5)
        statusCode = '200'
    except:
        statusCode = '404'

    setStatusCode(conn, pid, statusCode)
