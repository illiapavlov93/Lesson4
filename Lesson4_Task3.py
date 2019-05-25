def verifpas(a):
    sumnum = 0
    sumlet = 0
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    if len(a) > 4:
        for i in a:
            if i in chars:
                if i.isnumeric():
                    sumnum += 1
                elif i.isalpha():
                    sumlet += 1
            else:
                return print('пароль не валиден')
    if sumlet % 2 == 1 and sumnum % 2 == 0:
        print('пароль валиден')
    else:
        print('пароль не валиден')


password = 'lotwart45'
verifpas(password)
