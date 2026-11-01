# Циклы for
# 1. Все числа от 1 до 10
for i in range(1, 11):
    print(i)

# 2. Чётные числа от 2 до 50
for i in range(2, 51, 2):
    print(i)

# 3. Числа от 10 до 1 в порядке убывания
for i in range(10, 0, -1):
    print(i)

# 4. Сумма всех чисел от 1 до n
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)

# 5. Факториал числа n
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# 6. Таблица умножения на n от 1 до 10
n = int(input())
for i in range(1, 11):
    print(n * i)

# 7. Сколько положительных чисел в списке
numbers = [3, -1, 5, -7, 0, 8, -2, 4]
count = 0
for x in numbers:
    if x > 0:
        count += 1
print(count)

# 8. Количество гласных букв в строке
s = "Привет, мир!"
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)

# 9. Наибольший элемент списка без max()
numbers = [3, 17, 5, 42, 8, 11]
maximum = numbers[0]
for x in numbers:
    if x > maximum:
        maximum = x
print(maximum)

# 10. Таблица умножения от 1 до 9 в виде квадрата
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:3}", end=" ")
    print()

# Циклы while
# 1. Числа от 1 до 10 через while
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Сумма чисел до ввода 0
total = 0
while True:
    x = int(input())
    if x == 0:
        break
    total += x
print(total)

# 3. Количество цифр натурального числа
n = int(input())
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)

# 4. Сумма цифр натурального числа
n = int(input())
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)

# 5. Цифры в обратном порядке одним числом
n = int(input())
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)

# 6. Степени двойки, не превышающие n
n = int(input())
p = 1
while p <= n:
    print(p)
    p *= 2

# 7. Запрос пароля
correct = "qwerty"
password = input()
while password != correct:
    password = input()
print("OK")

# 8. НОД двух чисел
a = int(input())
b = int(input())
while b != 0:
    a, b = b, a % b
print(a)

# 9. Числа Фибоначчи, не превышающие n
n = int(input())
a, b = 0, 1
while a <= n:
    print(a)
    a, b = b, a + b

# 10. Угадай число
import random
secret = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input())
    attempts += 1
    if guess < secret:
        print("больше")
    elif guess > secret:
        print("меньше")
    else:
        print(attempts)
        break