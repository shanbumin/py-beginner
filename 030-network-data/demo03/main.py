

# 下面我们通过代码演示如何从豆瓣电影获取排前250名的电影的名称。
# 豆瓣电影Top250页面的结构和对应的代码如下图所示。 略   movie.douban.com/top250


import random
import re
import time

import requests

for page in range(1, 11):
    resp = requests.get(
        # 请求https://movie.douban.com/top250时，start参数代表了从哪一部电影开始
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出爬虫程序而阻止我们的请求
        # User-Agent可以设置为浏览器的标识（可以在浏览器的开发者工具查看HTTP请求头找到）
        # 由于豆瓣网允许百度爬虫获取它的数据，因此直接将我们的爬虫伪装成百度的爬虫
        headers={'User-Agent': 'BaiduSpider'}
    )
    # 创建正则表达式对象，通过捕获组捕获span标签中的电影标题
    pattern = re.compile(r'\<span class="title"\>([^&]*?)\<\/span\>')
    # 通过正则表达式获取class属性为title且标签内容不以&符号开头的span标签
    results = pattern.findall(resp.text)
    # 循环变量列表中所有的电影标题
    for result in results:
        print(result)
    # 随机休眠1-3秒，避免获取页面过于频繁
    time.sleep(random.randint(1, 3))



# 编写爬虫程序比较重要的一点就是让爬虫程序隐匿自己的身份，因为一般的网站都比较反感爬虫。
# 隐匿身份除了像上面的代码中修改User-Agent之外，还可以使用商业IP代理（如：蘑菇代理、芝麻代理等），让被爬取的网站无法得知爬虫程序的真实IP地址，也就无法通过IP地址对爬虫程序进行封禁。
# 当然，爬虫本身也是一个处于灰色地带的东西，没有谁说它是违法的，但也没有谁说它是合法的，本着法不禁止即为许可的精神，
# 我们可以根据自己工作的需要去编写爬虫程序，但是如果被爬取的网站能够举证你的爬虫程序有破坏动产的行为，那么在打官司的时候，基本上是要败诉的，这一点需要注意。

# 另外，用编写正则表达式的方式从网页中提取内容虽然可行，但是写出一个能够满足需求的正则表达式本身也不是件容易的事情，这一点对于新手来说尤为明显。
# 在下一节课中，我们将会为大家介绍另外两种从页面中提取数据的方法，虽然从性能上来讲，它们可能不如正则表达式，但是却降低了编码的复杂性，相信大家会喜欢上它们的。