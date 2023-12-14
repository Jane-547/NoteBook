
def create(base):
    try:
        file = open(base, 'r')
    except IOError:
        print('Создана новая записная книжка -> ' + base)
        file = open(base, 'w')
    finally:
        file.close()