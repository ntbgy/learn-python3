# CrowTaobaoPrice.py
import requests
import re


def getHTMLText(url):
    kv = {
        'cookie': '_m_h5_tk=74d5329e499da554596443bf19a86c60_1613149077598; _m_h5_tk_enc=4eda08e16ead5e0be35c01f0ffdb9c65; cna=+d6qGHGPEmACAW/jCiE4DXgg; t=fedad16d70ebd9cd1c1bf93ec5b0ab3e; sgcookie=E100C/bv57U8wmBvjIV3Avs7ot5k6g1Uod/gzMSQFAfipnXwQYZhlBUfxi/KID7fYWcEn+TMJiENQ8g6VYHqr99iaA==; uc3=vt3=F8dCuAc8LQQjo8iVeVk=&nk2=pf8I0+5Y5sEA&lg2=V32FPkk/w0dUvg==&id2=UU2w70qGOtGaWQ==; lgc=\u5E73\u5B89\u8DEF9\u53F7; uc4=nk4=0@p0jlz/z/N1CczreF96WEYWEI9dE=&id4=0@U2/32rYWgCPc7dkRhk5qG4D9oWiG; tracknick=\u5E73\u5B89\u8DEF9\u53F7; _cc_=Vq8l+KCLiw==; enc=HvmsbBGi/nP/UNn6c36P+o+zgcI8K4UeqFaACzZLAmFvb/PvjdYgAWU2cm5l7+jtPHzRMrM3rcfu4P51ZzjJDg==; hng=CN|zh-CN|CNY|156; thw=cn; mt=ci=7_1; xlly_s=1; uc1=cookie14=Uoe1gWJj/K/iNA==; cookie2=1517fc6fe32bb32864a1a60ee39c384d; _tb_token_=b577ed6b6563; JSESSIONID=71A48322A174FCA6036C9E52DAF4C39D; tfstk=c2HGBdw0_fP6f4PnNdws4e1LKSAdZZOa5xkELvKRiiZInxHFiO5FapQvxPK0xs1..; l=eB_wAahljaBFHGzkBOfZourza77OSIRYiuPzaNbMiOCP9NCp52lAW6iI40L9C3hVh6J2R38SZPt8BeYBqIv4n5U62j-la_kmn; isg=BO7uNA9RAvT_inabxBIrH17uP0Sw77LpTEEwHhi3WvGs-45VgH8C-ZT5smcXG6oB',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68'}
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            print(html)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
