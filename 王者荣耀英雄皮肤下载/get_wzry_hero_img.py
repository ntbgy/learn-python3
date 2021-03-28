#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import requests



def hero_img(hero_dir):
    if not os.path.exists(hero_dir):
        os.mkdir(hero_dir)
    url = 'http://pvp.qq.com/web201605/js/herolist.json'
    response = requests.get(url).content
    jsonData = json.loads(response)
    x = 0
    count = 1
    max = 0
    for m in range(len(jsonData)):
        ename = jsonData[m]['ename']
        cname = jsonData[m]['cname']
        title = jsonData[m]['title']
        skinName = list()
        skinName.append(title)
        temp = list()
        try:
            temp = jsonData[m]['skin_name'].split('|')
        except KeyError:
            pass
            # print(ename, cname, title, temp)
        for te in temp:
            if te in skinName:
                continue
            else:
                skinName.append(te)
        skinNumber = len(skinName)

        if len(skinName) == 7:
            print(count, cname, len(skinName), skinName)
        count += 1
        if skinNumber > max:
            max = skinNumber
        """
        for bigskin in range(1, skinNumber + 1):
            picUrl = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(
                ename) + '-bigskin-' + str(bigskin) + '.jpg'
            picture = requests.get(picUrl).content
            with open(hero_dir + cname + "-" + skinName[bigskin - 1] + '.jpg', 'wb') as f:
                f.write(picture)
                x = x + 1
                print("当前下载第 {} 张皮肤，{}-{}".format(str(x), cname, skinName[bigskin - 1]))
        """
    print(max)
def main():
    hero_dir = 'D:/王者荣耀-全英雄皮肤壁纸/'
    hero_img(hero_dir)


if __name__ == '__main__':
    main()
