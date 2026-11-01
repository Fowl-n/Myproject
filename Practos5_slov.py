# 1. Словарь учеников и оценок
students = {"Анна": 5, "Борис": 4, "Вика": 5}
name = "Борис"
print(f"Оценка {name}: {students[name]}")

# 2. Добавить / изменить / удалить пару
d = {"a": 1, "b": 2, "c": 3}
d["d"] = 4          # добавить
d["a"] = 10         # изменить
del d["b"]          # удалить
print(d)

# 3. Значение по ключу или «Нет такого ключа»
d = {"a": 1, "b": 2}
key = "c"
if key in d:
    print(d[key])
else:
    print("Нет такого ключа")

# 4. Ключи, значения и количество пар
d = {"a": 1, "b": 2, "c": 3}
print("Ключи:", list(d.keys()))
print("Значения:", list(d.values()))
print("Пар:", len(d))

# 5. Товары и цены с новой строки
products = {"хлеб": 40, "молоко": 80, "сыр": 300}
for name, price in products.items():
    print(f"{name}: {price}")

# 6. Сумма цен и самый дорогой товар
products = {"хлеб": 40, "молоко": 80, "сыр": 300}
total = 0
max_name = None
max_price = -1
for name, price in products.items():
    total += price
    if price > max_price:
        max_price = price
        max_name = name
print("Сумма цен:", total)
print("Самый дорогой:", max_name, "-", max_price)

# 7. Подсчёт символов в строке
s = "hello world"
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)

# 8. Подсчёт слов и самое частое
s = "яблоко банан яблоко груша банан яблоко"
counts = {}
for w in s.split():
    counts[w] = counts.get(w, 0) + 1
print(counts)
most_common = None
max_count = 0
for w, c in counts.items():
    if c > max_count:
        max_count = c
        most_common = w
print("Самое частое слово:", most_common, "-", max_count)

# 9. Обратный словарь (ключи ↔ значения)
d = {"a": 1, "b": 2, "c": 3}
rev = {v: k for k, v in d.items()}
print(rev)

# 10. Страны и столицы
countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
d = dict(zip(countries, capitals))
name = input("Введите страну: ")
if name in d:
    print("Столица:", d[name])
else:
    print("Нет такой страны")