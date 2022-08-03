#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from bs4 import BeautifulSoup
import requests

r = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())


with open('movies.txt', 'w') as f:
    titles = soup.find_all(name='h3', class_='title')
    for i in reversed(titles):
        f.write(i.text + "\n")
