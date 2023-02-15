import requests
from bs4 import BeautifulSoup
import json

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

#with open("food.html",  encoding="utf-8") as files:
    #datas = files.read()

#soup = BeautifulSoup(datas, "lxml")

#переменная с сылками 
#all_products_href = soup.find_all(class_="mzr-tc-group-item-href")

#словарь вида "Название категории":"URL"
#all_catigories_dict = {}

#пробегаем циклом и сохраняем данные в словарь
#for url in all_products_href:
    #item_text = url.text
    #item_url = "https://health-diet.ru" + url.get("href")
    #all_catigories_dict[item_text] = item_url

#with open("all_catigories_dict.json", "w", encoding='utf8') as all_catigories_json:
    #json.dump(all_catigories_dict, all_catigories_json, indent=4, ensure_ascii=False)

with open("all_catigories_dict.json", "w") as file:
    all_categories = json.load(file)