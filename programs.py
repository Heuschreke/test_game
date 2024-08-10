

import random
flag = True
while flag is True:
    num_z = random.randint(1, 100)
    print('Добро пожаловать в числовую угадайку')
    def is_valid(n):
        if n.isdigit() and 1 <= int(n) <= 100:
            return True
        else:
            return False
    a = 1
    while a > 0:
        n = input()
        if is_valid(n):
            num_p = int(n)
            break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
    s = 0
    while num_p != num_z:
        if num_p < num_z:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            num_p = int(input())
        elif num_p > num_z:
            print('Ваше число больше загаданного, попробуйте еще разок')
            num_p = int(input())
        s += 1
    print('Вы угадали всего лишь за', s, 'попыток,', 'поздравляем!')
    print('Хотите попробовать свои силы еще разок? Введите "да" или "нет"')
    otvet = input()
    if otvet == 'нет':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        flag = False
    if otvet == 'да':
        flag = True
