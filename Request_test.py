import re
import requests
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

res=requests.get('http://www.baidu.com')
file = open('html.html', 'w' )
file.write(res.text)
res.encoding='utf-8'
#print(res.text)

baidu = re.findall('<title>(.*?)</title>', res.text)

for i in baidu:
    print(i)

print(baidu[0])



