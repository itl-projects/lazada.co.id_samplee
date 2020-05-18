import requests
from bs4 import BeautifulSoup
import csv
import ast
import json


def Scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def data():
    final=[]
    value={}
    soup=Scrape('https://www.lazada.co.id/beli-handphone/?spm=a2o4j.home.categories.1.41631559a2pDEB&abtest=&item_id=160041961&pos=1&abbucket=&clickTrackInfo=07898747-0529-4cc8-bc96-fafbe38495b7__3443__160041961__static__0.1__164121__7253&up_id=160041961&from=hp_categories&acm=icms-zebra-5000383-2586217.1003.1.2262787&scm=1007.17253.164121.0&version=v2&aldid=UyxUJe5L')
    for i in soup.find_all('script'):
        # print(i)
        if "listItems" in str(i.string):
            x = str(i.string).split('listItems":[')[1]
            # print(x)
            for i in range(1,40):
                if '"name"' in str(x):
                    name = str(x).split('name":')[i].split('"')[1]

                if '"productUrl"' in str(x):
                    url = str(x).split('productUrl":')[i].split('"')[1]

                if '"image"' in str(x):
                    image = str(x).split('image":')[i].split('"')[1]

                if '"ratingScore"' in str(x):
                    rating = str(x).split('ratingScore":')[i].split('"')[1]

                if '"priceShow"' in str(x):
                    price = str(x).split('priceShow":')[i].split('"')[1]

                value={"name": name, "price": price, "rating": rating, "url": url, "imageUrl": image}
                final.append(value)

        data = append(final)

    return data

def append(data):
    list=[]
    list.append(data)
    return list

def appendtoCSV(list):
    input_file='data.csv'
    with open(input_file, mode='w',encoding='utf-8') as csv_file:
        fieldnames = ['name', 'price','rating','url','imageUrl']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in list:
            for x in i:
                writer.writerow(x)



appendtoCSV(data())