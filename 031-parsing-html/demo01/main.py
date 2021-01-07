import random
import time

from lxml import etree
import requests


# 下面我们用XPath解析方式改写之前获取豆瓣电影Top250的代码，如下所示。
for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={
            'User-Agent': 'BaiduSpider',
        }
    )
    tree = etree.HTML(resp.text)
    # 通过XPath语法从页面中提取需要的数据
    spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
    for span in spans:
        print(span.text)
    time.sleep(random.randint(1, 3))



