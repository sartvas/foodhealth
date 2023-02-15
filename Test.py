from bs4 import BeautifulSoup

with open(r"findex.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

title = soup.title.text
print(title)

user_name = soup.find("div", class_="user__name").find("span").text
print(user_name)

user_name_whith_id = soup.find("div", {"class":"user__name", "id":"23"}).find("span").text
print(user_name)

all_user_info = soup.find(class_="user__info").find_all("span")

for key in all_user_info:
    print(key.text)

social_urls = soup.find(class_="social__networks").find_all('a')

for key in social_urls:
    item_url = key.get('href')
    item_text = key.text
    print(f"Social network {item_text}: {item_url}")

#siblings = soup.find(class_="user__name").find_next_sibling
#siblings2 = soup.find(class_="user__name").find_previous_sibling
#print(siblings, siblings2)
