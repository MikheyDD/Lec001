# a = 5
# b = 5.89
# c = 'hello'
# print("{} - {} - {}" .format(a, b, c))

# print('введите первое число: ')
# a = int(input())
# b = int(input('введите второе число: '))
#
# print(a, ' + ', b, ' = ', a + b)

# username = input('Введите имя: ')
# if username == 'Маша':
#    print('Ура, это же Маша')
# elif username == 'Марина':
#    print('Я так ждал Вас, Марина!')
# elif username == 'Денис':
#    print('Денис - топ')
# else:
#    print('Привет,', username)

n = int(input())
flag = True
i = 2
while flag:
 if n % i == 0: # если остаток при делении числа n на i равен 0
    flag = False
    print(i)
 elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
    print(n)
    flag = False
 i += 1