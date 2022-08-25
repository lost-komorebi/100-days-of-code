#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from bs4 import BeautifulSoup
import requests
import csv


def get_html(page=1):
    base_url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/'
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
    r = requests.get(base_url + str(page), headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_data(soup):
    rows = soup.find_all('tr', class_='data-table__row')
    page_list = []
    for row in rows:
        row_list = []
        for column in row.find_all('td'):
            v = column.contents[1].text
            row_list.append(v)
        if len(row_list) == 6:
            page_list.append(row_list)
    return page_list


def has_next(soup):
    for i in soup.find_all('a', class_='pagination__btn'):
        if 'pagination__next-btn' in i.get(
                'class') and 'pagination__btn--off' not in i.get('class'):
            next_page = i.get('href').split('/')[-1]
            return next_page
    return False


def main():
    table = []
    soup = get_html()
    table.append(get_data(soup))
    while has_next(soup):
        next_page = has_next(soup)
        soup = get_html(next_page)
        table.append(get_data(soup))
    return table


def write_csv(data):
    with open('payscale_data.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([
            'Rank',
            'Major',
            'Degree Type',
            'Early Career Pay',
            'Mid-Career Pay',
            '% High Meaning'])
        for page in data:
            for row in page:
                csvwriter.writerow(row)


if __name__ == '__main__':
    data = main()
    write_csv(data)
