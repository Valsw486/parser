import random

# Пример словаря с английскими словами и их определениями
words = {
    "apple": "a round fruit of a tree",
    "banana": "a long curved fruit",
    "orange": "a round citrus fruit",
    "grape": "a small round fruit",
}

# Пример перевода слов и определений на русский
translations = {
    "apple": ("яблоко", "круглый фрукт дерева"),
    "banana": ("банан", "длинный изогнутый фрукт"),
    "orange": ("апельсин", "круглый цитрусовый фрукт"),
    "grape": ("виноград", "маленький круглый фрукт"),
}


def get_english_words():
    word = random.choice(list(words.keys()))
    return {
        "english_words": word,
        "word_definition": words[word]
    }


def translate_to_russian(word, definition):
    return translations[word]


def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        if word_dict is None:  # Проверяем, не произошла ли ошибка
            print("Не удалось получить слово. Попробуйте снова.")
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и определение на русский
        translated_word, translated_definition = translate_to_russian(word, word_definition)

        # Начинаем игру
        print(f"Значение слова (на русском) - {translated_definition}")
        user = input("Что это за слово? (на русском) ")
        if user == translated_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break  # Выходим из цикл