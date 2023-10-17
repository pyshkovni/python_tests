# Инициализационный файл

# импорты
from handlers import get_time_track, bubble_sort, quick_sort, ExternalResourceGetter


@get_time_track(precision=6)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


if __name__ == "__main__":
    # user_input = int(input("Введи число, которое нужно возвести в степень 5к: "))
    user_input = 1
    print(f"Количество цифр в числе {user_input} в степени 5к: {digits(user_input)}")

    print("Пример с тестированием сортировки пузырьком")
    # Есть ошибки!
    print(bubble_sort([3, 14, 0, 1, 6, 7, 9, 8, 7, 11, 6, 4, 0, 0, 2]))

    # # Как выявить ошибку в функции? проверяем с разными данными
    # bubble_sort([3, 14, 0, 1, 6, 7, 9, 8, 7, 11, 6, 4, 0, 0, 2])
    # bubble_sort([-3, 4, 5])
    # bubble_sort([])

    # # Либо описать как условия
    if bubble_sort([3, 14, 0, 1, 6, 7, 9, 8, 7, 11, 6, 4, 0, 0, 2]) != [0, 0, 0, 1, 2, 3, 4, 6, 6, 7, 7, 8, 9, 11, 14]:
        print('Ошибка!')
    if bubble_sort([-3, 4, 5]) != [-3, 4, 5]:
        print('Ошибка!')

    # # Оператор assert – возвращает ли функция указанное значение?
    # assert bubble_sort([3, 4, 2, 8, 1, 6, 4]) == [1, 2, 3, 4, 4, 6, 8]
    # assert bubble_sort([3, 4, 2, 8, 1, 6, 4]) == [1, 2, 3, 4, 4, 6, 8], "Не работает сортировка по возрастанию"

    # Помимо assert существуют, также, doc-тесты – тесты, хранящиеся в doc-строках функций
    # Посмотрите в документацию функции buble_sort.
    # Заметим, что функция bubble_sort сортирует наоборот. Необходимо просто заменить "<" на ">"

    print("Пример с тестированием быстрой сортировки")
    # Есть ошибки! "list out of range" и также нужно изменить функцию так, чтобы остались только уникальные значения
    # print(quick_sort([3, 14, 0, 1, 6, 7, 9, 8, 7, 11, 6, 4, 0, 0, 2]))

    # assert и doc-тесты выполняют одно сравнение.
    # Для того чтобы протестировать сложные программные проекты, можно использовать фреймворк unittest
    # Он помогает писать сложные тесты-проверки как классы.

    # Обратитесь к файлам в папке tests

    getter = ExternalResourceGetter(url="https://en.wikipedia.org/wiki/ISO_4217")

    data = getter.run()
    # print(data)
    with open("page.html", mode="a", encoding="utf-8") as file:
        for line in data:
            file.write(line)
