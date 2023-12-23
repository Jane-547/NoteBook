class View:

    @staticmethod
    def interface():
        print("ЗАПИСНАЯ КНИЖКА")
        print("1. Добавить новую заметку")
        print("2. Изменить заметку")
        print("3. Выбрать заметки за дату")
        print("4. Удалить заметку")
        print("5. Показать все заметки")
        print("6. Выход")
        choice = input("Введите цифру для дальнейших действий: ")
        return choice

    @staticmethod
    def ok():
        print("Изменения сохранены!:)" + '\n')

    @staticmethod
    def error():
        print("Нужно ввести число от 1 до 6")

    @staticmethod
    def welcome():
        print("Приложение 'Записная книжка'. Добро пожаловать!" + "\n" + "-----------------------------------------" + "\n" + "Выберите пункт меню:" + "\n")

    @staticmethod
    def goodbye():
        print('Ждем вас снова!')

    @staticmethod
    def add_new():
        return input("Введите название заметки: ")

    @staticmethod
    def add_body():
        return input("Введите текст заметки: ")

    @staticmethod
    def get_id_from_user():
        return int(input("Введите ID заметки: "))


    @staticmethod
    def change_title():
        return input("Введите новое название: ")

    @staticmethod
    def not_found():
        print("Заметка с таким Id не найдена!")

    @staticmethod
    def date_from_user():
        return input("Введите дату в формате ГГГГ-ММ-ДД: ")

    @staticmethod
    def show_notes(notes):
        for note in notes:
            print(note)
            print('***********************')

    @staticmethod
    def no_data_found():
        print("За эту дату заметок нет!")
