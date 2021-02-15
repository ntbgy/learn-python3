import requests


def getHTMLText(url, kv, 浏览器):
    try:
        r = requests.get(url, params=kv, headers=浏览器, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:5000]
    except:
        return "产生异常"


if __name__ == "__main__":
    url = 'https://www.so.com/s'
    浏览器 = {'user-agent': 'Mozilla/5.0'}
    kv = {'q': 'Python'}
    print(getHTMLText(url, kv, 浏览器))
