
def interface():
    print("ЗАПИСНАЯ КНИЖКА")
    print("1. Добавить новую заметку")
    print("2. Показать все заметки")
    print("3. Изменить заметку")
    print()
    choice = input("Введите цифру для дальнейших действий: ") 
    return choice


def ok():
    print("Изменения сохранены!:)" + '\n')

def error():
    print("Нужно ввести число от 1-6")


def welcome():
    print("Приложение 'Записная книжка'. Добро пожаловать!" + "\n" + "-----------------------------------------" + "\n" + "Выберите пункт меню:" + "\n")


def goodbye():
    print('Ждем вас снова!')