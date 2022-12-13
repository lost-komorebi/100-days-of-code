#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from bs4 import BeautifulSoup
import requests
import csv


def get_html(page=None):
    url = 'https://www.audible.com/search'
    if page:
        parameter = {'keywords': 'python', 'page': page}
    else:
        parameter = {'keywords': 'python'}
    r = requests.get(url=url, params=parameter).text
    soup = BeautifulSoup(r, 'html.parser')
    return soup


def has_next_page(soup):
    next_btn = soup.select("span[class*='nextButton']")
    if 'bc-button-disabled' in next_btn[0]['class']:
        return False
    return True


def get_next_page(soup):
    """get page number"""
    next_btn = soup.select("span[class*='nextButton']")
    return next_btn[0].select_one('a')['href'].rsplit('=', 1)[1]


def get_book_list_html(soup):
    book_list_html = soup.select('#center-3>div>div>div>span>ul>li')
    return book_list_html


def get_book_list(soup):
    book_list_html = get_book_list_html(soup)
    book_list = []
    for i in range(len(book_list_html)):
        title = get_attr(book_list_html[i], 'h3 > a')
        subtitle = get_attr(book_list_html[i], "li[class*='subtitle']>span")
        author = get_attr(book_list_html[i], "li[class*='authorLabel']>span>a")
        narrator = get_attr(
            book_list_html[i],
            "li[class*='narratorLabel']>span>a")
        length = colons_remover(
            get_attr(
                book_list_html[i],
                "li[class*='runtimeLabel']>span"))
        release_date = colons_remover(get_attr(
            book_list_html[i],
            "li[class*='releaseDateLabel']>span"))
        language = colons_remover(get_attr(
            book_list_html[i],
            "li[class*='languageLabel']>span"))
        rate = rate_formatter(get_attr(
            book_list_html[i],
            "li[class*='ratingsLabel']>span:nth-child(2)"))
        rate_number = rate_formatter(get_attr(
            book_list_html[i],
            "li[class*='ratingsLabel']>span:nth-child(3)"))
        price = get_attr(
            book_list_html[i],
            f"#buybox-regular-price-{i} > span:nth-child(2)").strip()
        book = {
            'title': title,
            'subtitle': subtitle,
            'author': author,
            'narrator': narrator,
            'length': length,
            'release_date': release_date,
            'language': language,
            'rate': rate,
            'rate_number': rate_number,
            'price': price,
        }
        book_list.append(book)
    return book_list


def colons_remover(string):
    """removing the colons in length, release_date, language"""
    if string:
        return string.split(':')[1].strip()
    return string


def rate_formatter(rate):
    if rate:
        return rate.split(' ')[0]
    return rate


def get_attr(element, css_selector):
    try:
        sub_element = element.select_one(css_selector)
        return sub_element.text
    except Exception:
        return ''


def write_csv(file, books_to_write: list):
    # add book detail to csv
    with open(file, 'a', newline='') as f:
        for book in books_to_write:
            f_writer = csv.writer(f)
            f_writer.writerow(book.values())


if __name__ == '__main__':
    filename = 'results.csv'
    soup_ = get_html()
    books = get_book_list(soup_)

    # add header to csv
    header = books[0].keys()
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()

    write_csv(filename, books)

    while has_next_page(soup_):
        page_number = get_next_page(soup_)
        print(page_number)
        soup_ = get_html(page_number)
        books = get_book_list(soup_)
        write_csv(filename, books)

