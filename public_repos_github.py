import requests
import json
from pprint import pprint

user = input('Введите имя пользователя: ')

#Сначала вычислим количество публичных репозитариев:
user_json = requests.get(f'https://api.github.com/users/{user}').json()
count_repos = user_json['public_repos']
print(f'\nимеется публичных репозиториев: {count_repos}\n')

# Устанавливаем параметры для запроса репозиториев:
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
params = {'per_page': count_repos}

main_link = (f'https://api.github.com/users/{user}/repos')
response = requests.get(main_link, headers=headers, params=params)
if response.ok:
	data = response.json()

# Выведем список ссылок на публичные репозитарии
k = 0
for i in data:
	k += 1
	print  (f'html репозитория № {k} :  {i["html_url"]}')

#Вывод в JSON списка репозиториев с данными
#pprint(data)
with open('public_repos.json', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=2)

#with open('public_repos.json') as f:
#    print(f.read())
