import requests

# Создаем словарь с данными для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

# Печатаем статус-код и содержимое ответа
print(f"Статус-код: {response.status_code}")
print("Содержимое ответа:")
print(response.json())
