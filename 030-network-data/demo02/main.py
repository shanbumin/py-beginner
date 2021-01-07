import requests

# todo 获取百度Logo并保存到名为baidu.png的本地文件中。
resp = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
with open('baidu.png', 'wb') as file:
    # 通过Response对象的content属性获取服务器返回的二进制内容
    file.write(resp.content)



