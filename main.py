import bs4
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

prod_name = []
prices = []
desc = []
reviews = []

for i in range(2, 5):
    r = requests.get(
        "https://www.flipkart.com/search?q=refrigerator+double+door&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_4_na_na_na&as-pos=3&as-type=RECENT&suggestionId=refrigerator+double+door&requestId=507861a0-33ca-4d98-bd7e-2d182da2875c&as-searchtext=refr&page=" + str(
            1))
    soup = bs(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")

    for i in names:
        name = i.text
        prod_name.append(name)

    price = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in price:
        name = i.text
        prices.append(name)

    des = box.find_all("ul", class_="_1xgFaf")
    for i in des:
        name = i.text
        desc.append(name)

    rev = box.find_all("div", class_="_3LWZlK")
    for i in rev:
        name = i.text
        reviews.append(name)

df = pd.DataFrame({"Product Name": prod_name, "Prices": prices, "Description": desc, "Reviews": reviews})
print(df)
df.to_csv("refrigerators.csv ")