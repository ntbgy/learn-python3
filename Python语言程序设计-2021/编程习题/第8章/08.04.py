#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def getText(地址):
    txt = open(地址, "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
    return txt


def 屏幕打印(word, counts, items, 打印行数):
    for i in range(打印行数):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


def 词频统计(hamletTxt):
    words = hamletTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    屏幕打印(word, counts, items, 5)


def main():
    地址 = "../txt/hamlet.txt"
    hamletTxt = getText(地址)
    词频统计(hamletTxt)


if __name__ == '__main__':
    main()
