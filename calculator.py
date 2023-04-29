lang = 'RU'
if lang == 'RU':
    f = 'Введите первое число:  '
    o = 'Введите операцию (+,-, /, *):  '
    s = 'Введите второе число:  '
    r = 'Результат: '
    e = 'Ошибка'
    v = 'Введите "yes", чтобы продолжить, и любую клавишу, чтобы закончить:  '
prodolzhit = 'yes'
while prodolzhit == 'yes':
    f_num = float(input(f))
    oper = input(o)
    sec_num = float(input(s))
    if oper == '+':
        print(r, f_num + sec_num)
    elif oper == '-':
        print(r, f_num - sec_num)
    elif oper == '/':
        print(r, f_num / sec_num)
    elif oper == '*':
        print(r, f_num * sec_num)
    else:
        print(e)
    prodolzhit = input(v)