import requests
import pprint

# Указываем параметры запроса
params = {
    'userId': 1
}

# Отправляем GET-запрос
response = requests.get('https://jsonplaceholder.typicode.com/posts',
                        params=params)

# Проверяем статус ответа
if response.ok:
    # Получаем и выводим JSON-ответ
    response_json = response.json()
    pprint.pprint(response_json)
else:
    print(f"Ошибка: {response.status_code}")