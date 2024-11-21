import re


def input_data():
    """Функция для ввода данных сотрудников."""
    try:
        with open('data.txt', 'a', encoding='utf-8') as file:
            while True:
                # Ввод фамилии и имени
                surname = input("Введите фамилию сотрудника (только буквы и возможный '-'): ").strip()
                name = input("Введите имя сотрудника (только буквы и возможный '-'): ").strip()

                # Проверка фамилии и имени
                if not re.fullmatch(r"[A-Za-zА-Яа-яЁё]+(-[A-Za-zА-Яа-яЁё]+)?", surname):
                    print("Фамилия должна содержать только буквы или одну черточку '-'.")
                    continue
                if not re.fullmatch(r"[A-Za-zА-Яа-яЁё]+(-[A-Za-zА-Яа-яЁё]+)?", name):
                    print("Имя должно содержать только буквы или одну черточку '-'.")
                    continue

                # Ввод количества детей
                children = input("Введите количество детей младше 18 лет (1-2 цифры): ").strip()

                # Проверка количества детей
                if not re.fullmatch(r"\d{1,2}", children):
                    print("Количество детей должно быть числом из 1 или 2 цифр.")
                    continue

                # Запись данных в файл
                file.write(f"{surname}\t{name}\t{children}\n")
                print("Данные успешно сохранены.")

                # Предложение продолжить или выйти
                another = input("Хотите ввести данные для другого сотрудника? (да/нет): ").strip().lower()
                if another != 'да':
                    break
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def view_data():
    """Функция для вывода данных из файла."""
    try:
        with open('data.txt', 'r', encoding='utf-8') as file:
            total_children = 0
            print("Список сотрудников:")
            print("Фамилия\tИмя\tКоличество детей")
            print("-" * 30)

            for line in file:
                data = line.strip().split('\t')
                if len(data) == 3:
                    surname, name, children = data
                    print(f"{surname}\t{name}\t{children}")
                    total_children += int(children)

            print("-" * 30)
            print(f"Общее количество детей: {total_children}")
    except FileNotFoundError:
        print("Файл с данными не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def main_menu():
    """Главное меню программы."""
    while True:
        print("\nМеню:")
        print("1. Ввод данных в файл")
        print("2. Просмотр данных из файла")
        print("3. Выход")

        choice = input("Выберите опцию (1/2/3): ").strip()
        if choice == '1':
            input_data()
        elif choice == '2':
            view_data()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main_menu()
