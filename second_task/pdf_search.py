import threading
import time
from queue import Queue
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

int_url = set()
result = []


def search_pdf_on_page(q):
    while True:
        url = q.get()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        print(f"Производится поиск на {url}")
        for link in soup.select("a[href$='.pdf']"):
            title = link.text.replace("\n", "").replace("\xa0", " ")
            if title in result:
                continue
            else:
                result.append(title)
        q.task_done()


def valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def website_links(url):
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = (
            parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        )
        if not valid_url(href):
            continue
        if href in int_url:
            continue
        if domain_name not in href:
            continue
        int_url.add(href)
    print(f"Найдено {len(int_url)} адресов на сайте.")
    return int_url


def main(url):
    q = Queue()
    website_links(url)
    for i in int_url:
        q.put(i)
    start_time = time.time()
    thread1 = threading.Thread(
        target=search_pdf_on_page, args=(q,), daemon=True
    )
    thread2 = threading.Thread(
        target=search_pdf_on_page, args=(q,), daemon=True
    )
    thread1.start()
    time.sleep(1)
    thread2.start()
    q.join()
    print(result)
    print(f"Найдено файлов: {len(result)}")
    print(f"Время выполнения программы: {time.time()-start_time} секунд.")


if __name__ == "__main__":
    main("https://cbr.ru/sitemap/")
