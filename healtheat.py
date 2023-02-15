import requests
from bs4 import BeautifulSoup

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
# }
# req = requests.get(url, headers=headers)
# src = req.text
# #print(src)
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

with open("food.html",  encoding="utf-8") as files:
    datas = files.read()

soup = BeautifulSoup(datas, "lxml")

all_products_href = soup.find_all(class_="mzr-tc-group-item-href")
all_catigories_dict = {}
for url in all_products_href:
    item_text = url.text
    item_url = "https://health-diet.ru" + url.get("href")
    all_catigories_dict[item_text] = item_url
print(all_catigories_dict)