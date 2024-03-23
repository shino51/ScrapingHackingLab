import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scrape_from_google_search():
    url = "https://www.yahoo.com"
    keyword = "Scraping"
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)
    driver.maximize_window()

    # Cookieの承認をする
    driver.find_element("name", "agree").click()

    search = driver.find_element("name", "p")
    search.send_keys(keyword)
    search.submit()

    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = soup.find_all("h3", attrs={"class": "title"})

    index = 1
    for result in results:
        # aria-label が貼られているものだけがタイトルなので、それが含まれているものだけ抽出する
        if result.select("a[aria-label]"):
            print("%d: %s " % (index, result.find("a")["aria-label"]))
            index += 1

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    scrape_from_google_search()
