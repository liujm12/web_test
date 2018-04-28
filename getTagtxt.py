import re
import requests
import sys
from lxml import etree

# reload(sys)
# sys.setdefaultencoding('utf-8')

res=requests.get('http://develop.dev.smosh.com/videos/no-you-get-over-it-3144588')
res.encoding='utf-8'
# print(res.text)

tags = re.findall('rel="tag">(.*?)</a>', res.text)
for i in tags:
    print(i)
