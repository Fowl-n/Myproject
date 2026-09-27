
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input(
"Выберите операцию: \n"
"   + Сложение\n"
"   - Вычитание\n"
"   * Умножение\n"
"   / Деление\n"
"   // Целочисленное деление\n"
"   % Остаток от деления\n"
"   ** Возведение в степень\n"
) or None
d = ['+', '-', '*', '/', '//', '%', '**']
if c in d:
    print("Такая операция есть")
if c is None:
    print("Операция не выбрана")
if c == "+":
    print(round(a+b))
elif c == "-":
    print(round(a-b))
elif c == "*" and a != 0 and b != 0:
    print(round(a*b))
elif c == "/" and b != 0:
    print(round(a/b))
elif c == "//" and b != 0:
    print(round(a//b))
elif c == "%" and b != 0:
    print(round(a%b))
elif c == "**":
    print(round(a**b))
else:
    print("Ошибка")