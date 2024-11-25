import time
from time import sleep
from threading import Thread
from datetime import datetime

# Функция записи слов в файл
def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды после каждой записи
    print(f"Завершилась запись в файл {file_name}")

# Основная часть программы
if __name__ == "__main__":
    # Замер времени для последовательного вызова функций
    start_time = datetime.now()

    # Последовательный вызов функций
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")

    end_time = datetime.now()
    print(f"Время выполнения последовательных функций: {end_time - start_time}")

    # Замер времени для работы потоков
    start_time = datetime.now()

    # Создание потоков
    threads = [
        Thread(target=write_words, args=(10, "example5.txt")),
        Thread(target=write_words, args=(30, "example6.txt")),
        Thread(target=write_words, args=(200, "example7.txt")),
        Thread(target=write_words, args=(100, "example8.txt")),
    ]

    # Запуск потоков
    for thread in threads:
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    end_time = datetime.now()
    print(f"Время выполнения потоков: {end_time - start_time}")