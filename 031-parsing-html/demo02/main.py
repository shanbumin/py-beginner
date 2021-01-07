import random
import time

import bs4
import requests

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={
            'User-Agent': 'BaiduSpider',
        }
    )
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    # 通过CSS选择器从页面中提取需要的数据
    spans = soup.select('div.info > div.hd > a > span:nth-child(1)')
    for span in spans:
        print(span.text)
    time.sleep(random.randint(1, 3))