#1
# Напишите программу, которая получает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# Каждое число записано в отдельной строке.
# a = int(input("введите длину катета : "))
# b = int(input("введите длину катета : "))
# s = (a * b)/2
# print(s)
# #2
# В школе решили набрать три новых математических класса.
# Так как занятия по математике у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты
# . За каждой партой может сидеть не больше двух учеников.
# Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
# a = int(input("количество учеников в классе А : "))
# b = int(input("количество учеников в классе Б : "))
# c = int(input("количество учеников в классе В : "))
# d = (a + b + c)/2
# print(d)
#3
# Даны три целых числа.
# Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
# number1 = int(input("введите первое число : "))
# number2 = int(input("введите второе число : "))
# number3 = int(input("введите третье число : "))
# if number1 == number2 and number2 == number3:
#     print("3")
# elif number1 == number2 or number2 == number3 or number3 == number1:
#     print("2")
# else:
#     print("0")
# #4
# Дано натуральное число.
# Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# number1 = int(input("Enter the year please "))
# if number1 %4 == 0 and number1 %100 !=100 or number1 %400 == 0:
#     print("YES")
# else:
#     print("NO")


#Камень ножницы бумага
player1_score = 0
player2_score = 0
player1_choise = ''
player2_choise = ''
rounds = 3