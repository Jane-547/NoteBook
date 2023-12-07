import module
import view


def start():
    view.welcome()
    path = "Phonebook.txt"
    module.create(path)
    while True:
        choice = view.interface()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6':
            view.error()
        elif choice == '1':
            contact = input('Введите имя и фамилию контакта: ')
            phonenumber = input('Введите телефонный номер контакта: ')
            module.add_cont(contact, phonenumber)
            view.ok()
        elif choice == '2':
            module.show_all()
        elif choice == '3':
            find = input('Введите Фамилию или номер контакта: ')
            module.search(find)
        elif choice == '4':
            fam = input('Введите текст для редактирования: ')
            module.change(path, fam)
        elif choice == '5':
            delcont = input('Введите строку для удаления: ')
            module.delete_contact(path, delcont)
        elif choice == '6':
            view.goodbye()
            break
