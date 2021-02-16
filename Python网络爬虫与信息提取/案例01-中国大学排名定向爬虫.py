#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            a = tr('a')
            tds = tr('td')
            ulist.append([tds[0].text.strip(), a[0].text.strip(), tds[4].text.strip(), ])


def printUnivList(ulist, num):
    print("{0:^10}\t{1:{3}^12}\t{2:^10}".format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print("{0:^10}\t{1:{3}^12}\t{2:^10}".format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/2020'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)


if __name__ == '__main__':
    main()
