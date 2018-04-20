import requests
res=requests.get('http://www.baidu.com')
res.encoding='utf-8'
print(res.text)