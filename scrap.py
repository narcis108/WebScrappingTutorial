import shutil
import urllib.request
import os
import sys
from bs4 import BeautifulSoup

PAGE_LINK = "http://opencube.ro"
ROOT_DIRECTORY = PAGE_LINK[7:]
ROOT_DIRECTORY_PATH = os.path.abspath(ROOT_DIRECTORY)
PAGES = int(sys.argv[1])


def get_url_content(url, file):
    with urllib.request.urlopen(url) as response, open(file, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def get_BS_page(url):
    http_response_object = urllib.request.urlopen(url)
    return BeautifulSoup(http_response_object, "html.parser")


def get_articles_urls(BS_page):
    articles_list = page.find_all("h2", class_="entry-title")
    list = [article.find("a")["href"] for article in articles_list]
    return list


def create_pages(page, page_number):
    current_directory = "{}/{}".format(ROOT_DIRECTORY, str(page_number))
    articles_list = get_articles_urls(page)
    if not os.path.exists(current_directory):
        os.makedirs(current_directory)
    for article_url in articles_list:
        get_url_content(article_url, "{}/{}.html".format(current_directory, article_url[19:len(article_url) - 1]))


if __name__ == '__main__':
    try:
        if len(sys.argv) < 1:
            raise Exception
        for page_number in range(1, PAGES + 1):
            if page_number == 1:
                page = get_BS_page(PAGE_LINK)
                create_pages(page, 1)
            else:
                page = get_BS_page("{}/page/{}/".format(PAGE_LINK, page_number))
                create_pages(page, page_number)
    except Exception:
        print('A aparut o eroare. Nu cumva nu ai introdus niciun argument in linia de comada? :)')
        s
