import requests

def getHTMLText(url, kv):
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[1000:2000]
    except:
        return "产生异常"

if __name__ == "__main__":
    url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
    kv = {'user-agent':'Mozilla/5.0'}
    print(getHTMLText(url, kv))

