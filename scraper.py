import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Apple-iPhone-Xs-Max-64GB/dp/B07J3CJM4N/ref=sr_1_2_sspa?keywords=iphone+xr&qid=1562926456&s=gateway&sr=8-2-spons&psc=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price(url=URL):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    #soup2 = BeautifulSoup(soup1, 'html.parser') #2 soups due to amazon.in

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()

    print(f"Product title: {title}, Price: {price}")

if __name__=='__main__':
    check_price(URL)