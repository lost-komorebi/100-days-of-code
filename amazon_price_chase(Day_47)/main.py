#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from bs4 import BeautifulSoup
import requests
import smtplib
url = "https://www.amazon.com/dp/B08YT3ZJC8/ref=ods_gw_ring_fam_im_rvdw/?pf_rd_r=XKQA8VAY31JMN4B5WXGV&pf_rd_p=dccb1950-0ab8-4ec0-a487-8be256059d2d&pd_rd_r=9f12d77c-7f3f-4b30-a4c3-a3bacd3792d9&pd_rd_w=ZHeVo&pd_rd_wg=ijTyT&ref_=pd_gw_unk&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.content, 'lxml')
price = float(
    soup.select_one(
        selector='span[class="a-price a-text-price a-size-medium"] > span[aria-hidden="true"]').text.split('$')[1])
title = soup.select_one(selector='#productTitle').text


if price < 100:

    my_email = 'to_fill'
    my_password = 'to_fill'
    to_email = 'to_fill'
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f'subject:price alert\n\n{title}\n now {price}\n {url}'.encode('utf-8'))
