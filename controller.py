import model
import view
import filehandler


def start():
    view.welcome()
    path = input('Введите название файла. Если он не существует, то будет создан: ')
    model.create(path)
    while True:
        choice = view.interface()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6':
            view.error()
        elif choice == '1':

        elif choice == '6':
            view.goodbye()
            break
