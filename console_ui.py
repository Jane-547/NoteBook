from NoteBook.controller import Controller


def start():
    ctrl = Controller()

    while True:
        ctrl.view.welcome()
        choice = ctrl.view.interface()
        if choice == '1':
            ctrl.add_note()
        elif choice == '2':
            ctrl.edit_note()
        elif choice == '3':
            ctrl.show_by_date()
        elif choice == '4':
            ctrl.delete_note()
        elif choice == '5':
            ctrl.show_all()
        elif choice == '6':
            ctrl.view.goodbye()
            break
        else:
            ctrl.view.error()
