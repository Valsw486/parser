import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем статус ответа

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except Exception as e:
        print("Произошла ошибка:", e)
        return None  # Возвращаем None в случае ошибки

# Создаём функцию для перевода слов на русский язык
def translate_to_russian(word, definition):
    translator = Translator()
    translated_word = translator.translate(word, dest='ru').text
    translated_definition = translator.translate(definition, dest='ru').text
    return translated_word, translated_definition

# Создаём функцию, которая будет делать саму игру
# def word_game():
#     print("Добро пожаловать в игру")
#     while True:
#         # Создаём функцию, чтобы использовать результат функции-словаря
#         word_dict = get_english_words()
#         if word_dict is None:  # Проверяем, не произошла ли ошибка
#             print("Не удалось получить слово. Попробуйте снова.")
#             break
#
#         word = word_dict.get("english_words")
#         word_definition = word_dict.get("word_definition")
#
#         # Переводим слово и определение на русский
#         translated_word, translated_definition = translate_to_russian(word, word_definition)
#
#         # Начинаем игру
#         print(f"Значение слова (на русском) - {translated_definition}")
#         user = input("Что это за слово? (на русском) ")
#         if user == translated_word:
#             print("Все верно!")
#         else:
#             print(f"Ответ неверный, было загадано это слово - {translated_word}")
#
#         # Создаём возможность закончить игру
#         play_again = input("Хотите сыграть еще раз? y/n: ")
#         if play_again.lower() != "y":
#             print("Спасибо за игру!")
#             break  # Выходим из цикла
#
# # Запускаем игру
# word_game()