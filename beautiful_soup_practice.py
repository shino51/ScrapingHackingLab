# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from bs4 import BeautifulSoup
import csv
import re


def fetch_on_this_day_from_wikipedia():
    url = "https://ja.wikipedia.org/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    today = soup.find("div", attrs={"id": "on_this_day"})

    entries = today.find_all("li")
    today_list = []

    for i, entry in enumerate(entries):
        today_text = entry.get_text().replace("（", "(").replace("）", ")")
        match = re.search(r'\((\d{3,4})年\)', today_text)
        if match:
            today_list.append([i + 1, entry.get_text(), match.group(1)])
        else:
            today_list.append([i + 1, entry.get_text()])

    with open("output.csv", "w", encoding="Shift_JIS") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerows(today_list)


def fetch_hatena_top_articles() :
    url = "https://b.hatena.ne.jp/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    top_entry = soup.find("section", attrs={"class": "entrylist-unit"})
    entries = top_entry.find_all("div", attrs={"class": "entrylist-contents"})
    for entry in entries:
        title_tag = entry.find("h3", attrs={"class": "entrylist-contents-title"})
        title = title_tag.find("a").get("title")
        users_tag = entry.find("span", attrs={"class": "entrylist-contents-users"})
        users = users_tag.get_text().strip()

        print(title)
        print(users)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fetch_on_this_day_from_wikipedia()