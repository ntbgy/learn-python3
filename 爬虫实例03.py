import requests

def getHTMLText(url, kv):
    try:
        r = requests.get(url, params=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:5000]
    except:
        return "产生异常"

if __name__ == "__main__":
    url = 'https://www.baidu.com/s'
    kv = {'wd':'Python'}
    print(getHTMLText(url, kv))

