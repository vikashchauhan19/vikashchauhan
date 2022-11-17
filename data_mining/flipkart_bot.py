import requests
import pandas as pd
from bs4 import BeautifulSoup

def get(url):
    page = requests.get(url)
    if page.status_code == 200:
        return  BeautifulSoup(page.text,'lxml')
    else:
        print('Error: ', page.status_code)
        return None



def extract(soup):
    target = soup.find('div',class_= '_1YokD2 _3Mn1Gg')
    products = target.find_all('div', class_= '_1AtVbE col-12-12')
    print("products:", len(products))
    info = []
    for item in products:
        name = item.find('div', class_= '_4rR01T')
        price = item.find('div', class_= '_30jeq3 _1_WHN1')
        old_price = item.find('div', class_= '_3I9_wc _27UcVY')
        ratings = item.find('div', class_= '_2_R_DZ')
        ratings_count = item.find('div', class_= '_13vcmD')
        data = {}
        try:
            data['name'] = name.text.strip()
        except:
            data['name'] = None
        try:    
            data['price'] = price.text.strip()
        except:    
            data['price'] = None
        try:    
            data['old_price'] = old_price.text.strip()
        except:    
            data['old_price'] = None
        try:    
            data['rating'] = ratings.text.strip()
        except:    
            data['rating'] = None
        try:    
            data['ratings_count'] = 'ratings_count'
        except:
            data['ratings_count'] = None
        info.append(data)
        print('Extracted:',name.text)
    return info     


def save(data):
    if len(data_list) > 0:
        pd.DataFrame(data_list).to_csv('flipkart.csv', index = False)
    else:
        print('No data to save')    




def main():
    pos = 1
    product = 'television'
    datalist = []
    while true:
        url = 'https://www.flipkart.com/search?q=television&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_2_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_2_na_na_na&as-pos=4&as-type=RECENT&suggestionId=television&requestId=c7e40dfc-3eb2-4676-8fcc-33f82536628f&as-backfill=on'
        print(url)
        soup = get(url)
        if soup:
            data = extract(soup)
            if data:
                datalist.extend(data)
                pos += 1
            else:
                break
        else:
            break        

main()        