# print(2+4)
# print("настя")

# if 1<2: 
#     print("Hello")
# else: 
#     print("f")

# #Регистрозависимость
# print("папа")
# #Print - неправильно

# # - строчные коментарии
# print("hdhd") #функции вывода данных в консольных

# ''' Блочные коментарии'''

# """ Блочные коментарии"""

# #print - функция для вывода информации на консоль
# print("Анна")

# print("Анна", 19,"Любит петь")

# #name = input("")
# #print(name)

# #Ключевое слово в питоне (по которым нельзя называть переменные)

# '''
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield
# '''

# # = знак присваивания
# name = "Настя"

# #PEP8

# #camel case
# userName="Анастасия"
# #underrscore notation
# user_name="Анастасия"

# age=15
# print(age)
# age=16
# print(age)

# #Типы данных

# #Числовые типы данных
# '''
# int- Целые числа x=5
# float - вешественный тип данных(число с плавающей точкой) y=5.6
# '''
# #Строчный
# '''
# str - Строка, состоящие из символов, заключенных одинарные или двойные кавычки
# name = "Фил"
# '''
# #Логический тип
# '''
# bool - Логические значения (True-истина,False-ложь)

# is_activate=True
# '''
# #Списки и коллекции
# #None
# '''
# NoneType- особый тип данных, который представляет отсутствие значения
# z=None
# '''
# z=2
# x=3.4
# is_activate=True
# d=None
# '''
# #2-10
# a=0b11
# print(a)
# b=0b1011
# print(b)
# c=0b100001
# print(c)

# #8-10
# a1=0o7
# a2=0o11

# #16-10
# a3=0x0A
# print(a3)


# x=10
# y=str(x)#Было числом стало строкой
# z=float(x)#Было числом стало вещественного типа
# print(x, y, z)

# s=2
# u=7
# sum=s+u
# print(sum)
# '''

# '''
# #Напишите программу, которая запрашивает имя пользователя и выводит приветствие: "Привет, [имя]!"
# name = input()
# print("привет", name, "!")
# '''
# '''
# #Пользователь вводит два целых числа. Программа выводит их сумму.
# а = int(input ("введите первое число"))
# b = int (input ("введите второе число"))
# print(a+b)
# summa=a+b
# print(summa)
# '''
# #Введите длину и ширину прямоугольника (числа с плавающей точкой). Выведите его площадь и периметр.
# """a=float(input("Введите длину"))
# d=float(input("Введите ширину"))
# print(a*d)
# print((a+d)*2)"""

# #Введите год рождения и текущий год. Выведите возраст пользователя (предполагаем, что день рождения уже был).
# """b_y=int(input('введите год рождения:'))
# n_y=int(input('введите текущий год'))
# age=n_y-b_y
# print(age)"""

# #Введите два числа. Поменяйте их местами и выведите результат (без использования третьей переменной).
# '''
# a=float(input("Введите число"))
# d=float(input("Введите число"))
# print(a+b)

# print(a+b)
# '''


# #Блок 1
# a=int()
# b=float()
# c=str()
# d=bool()
# e=None
# print(type(a), a)
# print(type(b), b)
# print(type(c), c)
# print(type(d), d)
# print(type(e), e)

# Age = 24 
# age = 15
# print(Age, age)

# #Выводится 24 и 15 соответственно переменных Age и age


# b=0b1101
# o=0o17
# x=0x1F
# print(b, o, x)

# #Блок 2
# a=str(25)
# print(a)
# b=float(a)
# print(b)
# c=int(b)
# print(c)

# name=input('Введите ваше имя: ')
# print('Привет', name)

# n1=float(input("Введите первое число: "))
# n2=float(input("Введите второе число: "))
# print(n1+n2, n1-n2, n1*n2, n1/n2)

# n1=float(input("Введите длинну: "))
# n2=float(input("Введите ширину: "))
# print('Периметр:', 2*(n1+n2), '\nПлощадь:',  n1*n2)


# a=int(input("Введите год рождения: "))
# b=int(input("Введите текущий год: "))
# print('Вам', b-a)

# a=input("Введите число: ")
# d=input("Введите число: ")
# print(b, a)

# #Блок 3
# a=input("Введите первое число: ")
# b=input("Введите второе число: ")
# c=str(input("Введите операцию: "))
# if c=='+': print(a+b)
# elif c=='-': print(a-b)
# elif c=='*': print(a*b)
# elif c=='/': print(a/b)
# else: print('Такой операции нет!')

# s=int(input("Введите количество секунд:"))
# m=s/60
# h=m/60
# print('Часы:', h, '\nМинуты:', m, '\nСекунды', s)

# money=float(input('Введите сумму в рублях:'))
# dollars=float(money*0.011855)
# evro=float(money*0.010174)
# print('Рубли:', money, '\nДоллары', dollars, '\nЕвро', evro)

# r=float(input('Введите радиус круга: '))
# print(2*3.14*r, 3.14*r*r)

# name=str(input('Введите имя: '))
# age=int(input('Введите возраст: '))
# print(name, ', через 10 лет вам будет ', age+10, 'лет')


# ##Введите два числа. Поменяйте их местами и выведите результат (без использования третьей переменной).

# #Комплексные числа
# complexNumber=1+2j
# print(complexNumber)

# ''' Управляющие последовательности в строке

# # Строка может содержать ряд специальных символов - управляющих последовательностей. 

# # Некоторые из них:

# # \\: позволяет добавить внутрь строки слеш

# # \': позволяет добавить внутрь строки одинарную кавычку

# # \": позволяет добавить внутрь строки двойную кавычку

# # \n: осуществляет переход на новую строку

# # \t: добавляет табуляцию (4 отступа)

# # '''

# text="Сообщение: \n\"Hello, my friends\""
# print(text)
# text1="Сообщение: \t\"Hello, my friends\""
# print(text1)



# # print("heog",end=" rbmum ")
# # print("wbho")


# #Операторы в программирование

# #Арифметические операторы

# #+ - / *
# # // - целочисленное деление
# # % - деление с остатком
# # ** - возведение в степень

# print(4+5)
# print(4-5)
# print(6*8)
# print(12/5)
# print(12//5)
# print(25%3)
# print(2**2)


# # Операции направления

# # ** - справо налево

# # * / // % - слева направо

# # +- -слева направо

# number= 3 + 4 * 5 ** 2 + 7
# # 1 шаг
# # 5 ** 2=25
# # 2 war
# # 25*4=100
# # 3 war
# # 100+3=103
# # 4 war
# # 103+7=110
# print(number)

# number= (3 + 4) * (5 ** 2 + 7)
# print(number)

# #Арифмитические операции с присвоением

# # +=
# # -=
# # /=
# # *=
# # //=
# # %=
# # **=


# number=10
# number+=5
# number-=5
# number/=5

# #Округление round

# first_num=2.0001
# sec_num=5
# third=first_num/sec_num
# print(third)
# print(round(2.0001+0.1))
# print(round(2.0001+0.1, 2))


# print(round(4.6759940+9.77993,3))



# # операторы сравнения

# print(2>3)  #больше
# print(3==3) #равно
# print(2!=9) #не равно
# print(3>=3) #больше или равно
# print(3<4)  #меньше
# print(4<=5) #меньше или равно

# # Лог операции

# # and - два истинна обязательно!
# # ог - хотя бы одно выражение должно быть истинно
# # not - инверсия (например, было ложно станет правдой)

# age=23
# isMarried= True
# print(not age >21)
# print(not isMarried)

# result= (5 == 5) and (6<7)
# print(result)

# result= (5 == 5) or (6<7)
# print(result)

# # значение in набор_значений

# # значение in набор_значений

# message="Русский квас"
# print("Русский" in message)

# print("лимонад" not in message )

# s=[1,2,3,4,5]
# print(6 in s)
# print(1 in s)

# x=[1,2,3]
# y=x
# print(x is y)



# x=[3,2,1]
# y=[1,2,3]
# print(x is not y)

# x=[1,2,3]
# y=[1,2,3]
# print(x == y)

# number = 10
# number+= 5
# number-= 3
# number*= 2
# number/= 4
# number//= 2
# number%= 3
# number**= 2




# if ycлoвиe:
#     блок кода, который выполняется если условие=True
# следующий блок кода


# x=4
# if x>5:
#     print ("х больше 5")


# buh=45

# money=int(input("сколько денег с собой? "))

# if money>=buh:
#     print ("вы можете купить булку")


# # Оператор if-else

# # if условие:
# #     блок кода1, выполнится если условие истино
# # else:
# #     блок кода 2, выполнится если предудыщие условие было ложно



# x=4
# if x>=5:
#     print("х больше 5")
# else:
#     print("x не больше 5")


# buh=45

# money=int(input("сколько денег с собой? "))

# if money>=buh:
#     print("вы можете купить булку")
# else:
#     print("недостаточно средств")



# x=15
# if x>10:
#     print ("х больше 10")
#     if x>20:
#         print ("х больше 20")
#     else:
#         print("x>10 но меньше или равно 20")
# else:
#     print ("x меньше или равно 10")


# language="английский"
# daytime="yтpo"
# if language == "английский":
#     print("English")
#     if daytime == "yтpo":
#         print("Good morning")
#     else:
#         print("Good evening")
# else:
#     if daytime == "yтpo":
#         print ("Доброе утро")
#     else:
#         print("Добрый вечер")


# # if -проверяет первое условие
# # elif- (сокращенное от else if) проверяет следующие условия, если предыдущее было ложно
# # else: - выполнеят бло кода, если все предыдущие были ложны

# # if условие1:
# #     блок кода1
# # elif ycnoвиe2:
# #     блок кода2:
# # elif условие3:
# #     блок кодаЗ:
# # else:
# #     блок кода4


# X=1
# if x>10:
#     print ("х больше 10")
# elif x>5:
#     print ("х больше 5 но меньше или равно 10")
# elif x>0:
#     print ("х больше 0, но меньше или равно 5")
# else:
#     print ("x меньше или равно 0")



# age=int(input("ваш возраст "))
# if age<1:
#     print ("введен некоректный возраст")
# elif age<18:
#     print("доступны мелоддрамы и комедии")
# elif age>=18:
#     print ("доступны к просмотру фильмы 18+")
# else:
#     print("Спасибо за заказ")


# x=5
# if x>=6:
#     print("привет")
# else:
#     print ("пoкa")
# print ("нет привет")


#Тернарный оператор

# x=10
# result="x больше 5" if x>5 else "x не больше 5"
# print(result)



# print ("Введите первую и последнюю букву русского афавита")
# first_letter=input()
# last_letter=input()


#Сокращенная запись
# if x>=0 and x<100: было
# if 0 <= x <100: стало



# a = int(input("Введите число: "))
# if (a%2) == 0: print("Число четное")
# else: print("Число нечетное")

# Пользователь вводит балл (0–100). Выведите оценку:

# 90–100 → «Отлично»
# 75–89 → «Хорошо»
# 60–74 → «Удовлетворительно»
# 0–59 → «Неудовлетворительно»

# a = int(input("Введите балл: "))
# if 0<=a<=59: print("«Неудовлетворительно»")
# elif 60<=a<=74: print("«Удовлетворительно»")
# elif 75<=a<=89: print("«Хорошо»")
# elif 90<=a<=100: print("«Отлично»")
# else: print("Такого балла нет")


# # Строки в Python - это последовательности символов, заключённые в одинарные
# # ( ' ... ' ), двойные ( " ... " ), тройные одинарные ( ''' ... ''' ) или тройные двойные
# # ( """ ... """ ) кавычки. Они представляют собой неизменяемые (immutable) типы данных,
# # что означает, что после создания строки её содержимое нельзя изменить.


# str1="Привет"
# str1='Привет'
# str1='''Привет'''
# str1="""Привет"""


# # p y t h o n
# # 0 1 2 3 4 5
# #  -5-4-3-2-1

# h="python"
# print(h)
# print (h[0])

# # h[0]="P"
# # print(h)

# # срез-это операция которая позволяет скопировать часть исходной строки, списка, кортежа
# print (h[::])


# # последовательность [start:stop:step]

# # start- начало индекса( включительно). По умолчанию с индекса 0
# # stop - индекс конца( не включительно). По умолчанию длина последовательности
# # step - шаг(через сколько элементов/символов брать). По умолчанию 1




# # p y t h o n
# # 0 1 2 3 4 5 положительный индекс
# #-6-5-4-3-2-1 отриц индекс

# print(h[0:3])
# print(h[:3])
# print(h[2:5])
# print(h[3:6])
# print(h[3:])
# print(h[::2])
# print(h[1::2])
# print(h[::-1])
# print(h[-4:-1])


# s="hello"
# s1="H" + s[1:]
# print(s1)



# S="привет"
# s1="марина"
# print(s+ " " +s1)

# print(s*7)


# # name=input ("Введите имя")
# # print(f"имя: {name}")


# print("изменение регистра")
# hello="hello world"
# print(hello.upper())
# print(hello.lower())
# print(hello.capitalize())
# print(hello.title())
# print(hello.swapcase())


# print ("поиск и проверка")
# print(hello.find("WORLD"))
# print(hello.startswith("h"))
# print(hello.endswith("D"))
# print(hello.count("R"))


# print ("замена и удаление пробелов")
# hello="     hello WORLD     "
# print(hello.strip())
# print(hello.rstrip())
# print(hello.lstrip())
# print(hello.replace("l", '1'))


# print ("выравнивание")
# print(hello.rjust(20))
# print(hello.ljust(30))
# print(hello.center(100))


# print("apple" == "banana")
# print("apple">"banana")


# S="hello"
# for i in s:
#     print(i)

# s="apple"
# s1="apple"
# print(s is s1)


# S=1
# s1=1
# print(s1 is s)


# print("你好")


# s=ord("G")
# print(s)


# s=chr(s) 
# print(s)


# # Списки в Python - это изменяемые последовательности элементов,
# # которые могут содержать данные любого типа: числа, строки,
# # другие списки и даже объекты. Списки позволяют хранить упорядоченные
# # коллекции элементов, доступ к которым можно получить по индексу.

# my_list=[1,2,3,5.6, True, "g", [1, 2, 3] ]
# print(my_list)

# my_list1=[]
# print(my_list1)

# my_list.append(4)
# print(my_list)

# my_list.insert(1,"двa")
# print(my_list)

# my_list.extend([3,4])
# print(my_list)

# my_list.remove(4)
# print(my_list)


# last_element=my_list.pop()
# print(last_element)
# print(my_list)


# my_list.clear()
# print(my_list)


# list1=[1,2,3,4]
# d=list1.index(2)
# print(d)


# count=list1.count(1)
# print(count)


# list2=[1,5,6,7,2,1,4]
# list2.sort()
# print(list2)

# list2=[1,5,6,7,2,1,4]
# list2.sort(reverse=True)
# print(list2)

# list4=[1,2,3,1]
# list4. reverse()
# print(list4)


# list2=[1,5,6,7,2,1,4]
# sorted=sorted(list2)
# list2.sort()
# print(list2)
# print(sorted)


# list2=[1,5,6,7,2,1,4]
# print(len(list2))

# print(list4[0])
# print(list4[2])


# list5=[1,2,3,4, [1,2]]
# print(list5[0])
# print(list5[2])
# print(list5[4] [1])



# кортеж-это последовательность элементов неизменняемого типа

t=('анна',4)
print(t)


t1='анна',4


t=('анна',)

data=["Анна",14]
anna=tuple(data)
print(data)
print(anna)

print(len(anna))



s=('анна',4,'петр',13)
print(s[0])
print(s[-1])
print(s[1])


# s[0]='hello'




# a=[1,2,3]
# a,b,c=a
# print(a)
# print(b)
# print(c)

 
# b=[1,2,3,4,5]
# a,*b,c=b
# print(a)
# print(b)
# print(c)

# c=[1,2,3,4,5]
# _,*b,c=c
# print(b)
# print(c)


s=('анна',44,'МПТ','методист')
name, age, company, postion=s
print(name)
print(age)
print(company)
print(postion)



t=('анна',44,'МПТ','методист')
print(t[1:3])
print(t[:2])
print(t[1:])
print(t[:])


user=('анна',44,'МПТ','методист')
name='анна'
if name in user:
    print("пол найден")
else:
    print("пол не найден")


# множество-хранит уникальные элементы(неупорядоченная коллекция элементов)


user={"Анна",56,"Анна"}
print(user)

# user={}


users=set()
print(users)

d=[1,2,3,3]
s=set(d)
print(s)


print(len(s))


fruits=set()
fruits.add("БАНАН")
print(fruits)


age={12,34,56,78,90}
number=34
if number in age:
    age.remove(number)
print(age)


age.discard(3)
print(age)




age.clear()
print(age)

age1={12,34,56,78,90}
for a in age1:
    print(a)

number_age=age1.copy()
print(number_age)


fruit1={"банан", "апельсин", "абрикос", "яблоко"}
fruit2={"вишня", "арбуз", "дыня"}
fruits=fruit1.union(fruit2)
print(fruits)
print(fruit1 | fruit2)


fruit1={"банан", "апельсин", "абрикос", "яблоко"}
fruit2={"вишня", "арбуз", "дыня", "абрикос"}
fruits2=fruit1.intersection(fruit2)
print(fruit2)

print(fruit1 & fruit2)

fruit1={"банан", "апельсин", "абрикос", "яблоко"}
fruit2={"вишня", "арбуз", "дыня", "абрикос"}
fruits3=fruit1.difference(fruit2)
print(fruits3)


print(fruit1-fruit2)

fruit1={"банан","апельсин", "абрикос", "яблоко"}
fruit2={"вишня", "арбуз", "дыня", "абрикос"}
fruits4=fruit1.symmetric_difference(fruit2)
print(fruits4)



print(fruit1^fruit2)



fruit1={"банан", "апельсин", "абрикос", "яблоко"}
fruit2={"вишня", "арбуз", "дыня", "абрикос", "банан", "апельсин", "яблоко"}
# Подмножество
print(fruit1.issubset(fruit2))
print(fruit2.issubset(fruit1))

# Надмножество
print(fruit1.issuperset(fruit2))
print(fruit2.issuperset(fruit1))

users=frozenset({"Анна", "петр","екатерина"})
print(users)

users=frozenset(["Анна", "петр","екатерина"])
print(users)

users=frozenset(("Анна", "петр","екатерина"))
print(users)

# Обработка исключений


str1="5"
integ=int(str1)
print(integ)

# str1="hello"
# integ=int(str1)
# print(integ)

# numberStr=input("введите число")
# numberInt=int(number)
# print(numberInt)




# try:
#     инструкция
# except [тип исключения]:
#     инструкция



# try:
#     numberStr=input("введите число")
#     numberInt=int(number)
# except:
#     print("Преобразование не получилось")
# print ("завершение программы")


# try:
#     number=int(input("введите число "))
#     print(number)
# except:
#     print ("преобразлование не получилось")
# finally:
#     print ("блок try завершил исключение")
#     print ("завершение программы")


# try:
#     numberStr=input("введите число")
#     numberInt=int(number)
# except ValueError:
#     print("Преобразование не получилось")
# except ZeroDivisionError:
#     print ("преобразлование не получилось") 
# except BaseException:
#     print ("преобразлование не получилось") 
# print ("завершение программы")


# try:
#     num1=input("введите 1 число: ")
#     num2=input("введите 2 число: ")
#     print(num1/num2)
# except ValueError:
#     print("Преобразование не получилось")
# except ZeroDivisionError as e:
#     print ("Попытка деления на ноль невозможна", e) 
# except BaseException:
#     print ("преобразлование не получилось") 
# print ("завершение программы")


try: 
    age=int(input ("Введите возраст"))
    if age> 100 or age<1:
        raise Exception("неккоретный ввод")
    print(age)
except ValueError:
    print("Введены неккоректные данные")
except Exception as e:
    print(e)
finally:
    print ("Завершение программы")




