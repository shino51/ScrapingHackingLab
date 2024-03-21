import urllib
from urllib import parse

import requests
from bs4 import BeautifulSoup
from reppy.robots import Robots


def reppy_practice():
    robots = Robots.fetch("https://allabout.co.jp/robots.txt")
    agent = robots.agent("*")
    is_allowed = agent.allowed("https://allabout.co.jp/ranking/daily/")
    print(is_allowed)


def get_user_agent():
    url = "http://httpbin.org/user-agent"
    user_agent = requests.get(url).text
    print(user_agent)


def get_relative_url():
    url = "https://kakaku.com"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    category_url = soup.find("a", attrs={"class": "p-catList_cell"}).get("href")
    long_category_url = urllib.parse.urljoin(url, category_url)

    print(long_category_url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_relative_url()
