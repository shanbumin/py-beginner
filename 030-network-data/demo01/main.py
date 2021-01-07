import requests



# todo 获取搜狐网首页。
# requests的get函数会返回一个Response对象
resp = requests.get('https://www.sohu.com/')
if resp.status_code == 200:
    # 通过Response对象的text属性获取服务器返回的文本内容
    print(resp.text)
