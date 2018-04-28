import requests
import ssl
from lxml import etree


# ssl._create_default_https_context = ssl._create_unverified_context

# session = requests.Session()
# URL = "http://www.smosh.com/"
# req = session.get(URL)
#
# req.encoding = 'utf8'
# root = etree.HTML(req.content)
# items = root.xpath('//ol/li/div[@class="item"]')


ssl._create_default_https_context = ssl._create_unverified_context

session = requests.Session()
for id in range(0, 251, 25):
    URL = 'https://movie.douban.com/top250/?start=' + str(id)
    req = session.get(URL)
    req.encoding = 'utf8'
    root = etree.HTML(req.content)
    items = root.xpath('//ol/li/div[@class="item"]')
    for item in items:
        rank, name, alias, rating_num, quote, url = "", "", "", "", "", ""
        try:
            url = item.xpath('./div[@class="pic"]//a/@href')[0]
            rank = item.xpath('./div[@class="pic"]/em/text()')[0]
            title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
            name = title[0].encode('gb2312', 'ignore').decode('gb2312')
            alias = title[1].encode('gb2312', 'ignore').decode('gb2312') if len(title) == 2 else ""
            rating_num = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
            quote_tag = item.xpath('.//div[@class="bd"]//span[@class="inq"]')
            if len(quote_tag) is not 0:
                quote = quote_tag[0].text.encode('gb2312', 'ignore').decode('gb2312')
            print(rank, rating_num, quote)
            print(name,alias)
        except:
            print('faild!')
            pass