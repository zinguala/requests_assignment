import requests

res = requests.get('https://randomuser.me/api/')
print(res)
ips = res.json()
print(ips)