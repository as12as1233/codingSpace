import requests

url = 'http://www.baidu.com'

rev = requests.get(url=url)

rev.encoding = 'utf-8'

print(rev.text)