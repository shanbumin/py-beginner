import requests

resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
print(type(resp))
print(resp)
# if resp.status_code == 200:
#     data_model = resp.json()
#     for news in data_model['newslist']:
#         print(news['title'])
#         print(news['url'])
#         print('-' * 60)




