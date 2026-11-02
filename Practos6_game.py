import time
import sys


def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()


def show_inventory(inventory):
    if not inventory:
        print("Ваш инвентарь пуст.")
    else:
        print(f"В инвентаре: {', '.join(inventory)}")


def check_item(inventory, item):
    return item in inventory


def level_one(inventory):
    print_slow("\nУРОВЕНЬ 1: Лесная прогулка")
    print_slow("Вы — маленький паучок. Ваша цель — перебраться на соседнее дерево.")
    print_slow("Но вокруг летают хищные жуки. Вам нужно найти защиту и способ перебраться.")

    locations = {
        "полянка": "Вы на стартовой полянке. На севере густой куст.",
        "куст": "Вы в кусте. Здесь лежит старая коряга (палка).",
        "ветка": "Вы на ветке. Впереди паутина, ведущая к цели."
    }
    current_loc = "полянка"
    found_items = set()

    while True:
        print(f"\nЛокация: {current_loc.capitalize()}")
        print(locations[current_loc])

        if current_loc == "куст" and not check_item(inventory, "палка") and "палка" not in found_items:
            print_slow("Вы видите на земле сухую палку. Она может пригодиться.")

        command = input("Введите команду (идти, взять, инвентарь, атаковать, выход): ").lower().strip()

        if command == "выход":
            return False
        elif command == "инвентарь":
            show_inventory(inventory)
        elif command == "идти":
            if current_loc == "полянка":
                current_loc = "куст"
                print_slow("Вы пробираетесь сквозь листву.")
            elif current_loc == "куст":
                current_loc = "ветка"
                print_slow("Вы карабкаетесь по стволу наверх.")
            elif current_loc == "ветка":
                if not check_item(inventory, "паутина"):
                    print_slow("На ветке есть паутина, но она порвана. Нужно сплести новую.")
                    print_slow("Для этого нужна палка.")
                    if not check_item(inventory, "палка"):
                        print_slow("Вы не сможете спуститься, так как внизу все заполонили красные муравьи.")
                        print_slow("Поблизости нет палок. Это конец.")
                        return False
                else:
                    print_slow("Вы перебираетесь по паутине на дерево и проходите уровень!")
                    return True
        elif command == "взять":
            if current_loc == "куст" and not check_item(inventory, "палка") and "палка" not in found_items:
                inventory.append("палка")
                found_items.add("палка")
                print_slow("Вы взяли палку. Теперь у вас есть оружие!")
            else:
                print_slow("Здесь нечего брать.")
        elif command == "атаковать":
            if current_loc == "ветка" and not check_item(inventory, "паутина"):
                if check_item(inventory, "палка"):
                    inventory.remove("палка")
                    inventory.append("паутина")
                    print_slow("Вы используете палку, чтобы плести паутину... Вы сплели прочную паутину!")
                else:
                    print_slow("У вас нет палки для плетения.")
            elif check_item(inventory, "палка"):
                print_slow("Вы бьете палкой по кустам, но там никого нет.")
            else:
                print_slow("Вам нечем атаковать.")
        else:
            print_slow("Неизвестная команда.")


def level_two(inventory):
    print_slow("\nУРОВЕНЬ 2: Паутина и Тьма")
    print_slow("Вы попали в темный угол леса. Выход закрыт гигантским пауком.")
    print_slow("Вам нужно отвлечь его или победить.")

    coordinates = (10, 20)
    inventory.append("лист")
    print_slow("Вы находите зеленый лист и кладете его в инвентарь.")

    solved_riddles = set()
    riddle_answer = "муха"

    while True:
        print_slow("\nЧто вы будете делать?")
        print_slow("Доступные действия: осмотреться, поймать, загадка, инвентарь, бежать")

        command = input("Ваш выбор: ").lower().strip()

        if command == "выход":
            return False
        elif command == "инвентарь":
            show_inventory(inventory)
        elif command == "осмотреться":
            if not check_item(inventory, "светлячок"):
                print_slow("Вы видите светлячка, летающего неподалеку. Он может дать свет.")
                print_slow("В темноте сверкают глаза паука.")
            else:
                print_slow("Светлячок освещает путь. Паук боится света!")
        elif command == "поймать":
            if not check_item(inventory, "светлячок"):
                inventory.append("светлячок")
                print_slow("Вы поймали светлячка! Теперь у вас есть источник света.")
            else:
                print_slow("Вы уже поймали светлячка.")
        elif command == "загадка":
            if check_item(inventory, "светлячок"):
                print_slow("Светлячок шепчет вам загадку: 'Кто всю жизнь летает, но никогда не устает?'")
                ans = input("Ответ: ").lower().strip()
                if ans == riddle_answer:
                    print_slow("Верно! Светлячок соглашается помочь вам и вы его отпускаете (он летает вокруг вас и освещает небольшую область).")
                    solved_riddles.add(riddle_answer)
                else:
                    print_slow("Неверно. Светлячок грустнеет.")
            else:
                print_slow("Вам не с кем говорить.")
        elif command == "бежать":
            if check_item(inventory, "светлячок"):
                print_slow("Вы бежите на свет светлячка и выбираетесь из ловушки!")
                print_slow("Уровень пройден!")
                return True
            else:
                print_slow("Вы пытаетесь бежать в темноте, но натыкаетесь на паутину и запутываетесь.")
                print_slow("Вы замечаете огромного паука, который пришел посмотреть, что попалось в его паутину.")
                print_slow("Он видет вас и бесжалостно съедает.")
                return False
        else:
            print_slow("Неизвестная команда.")


def level_three(inventory):
    print_slow("\nУРОВЕНЬ 3: Финальный рывок")
    print_slow("Вы почти у цели, но перед вами глубокая лужа.")
    print_slow("Нужно перебраться через нее, используя подручные средства.")

    commands = ["прыгнуть", "плыть", "мост", "инвентарь", "выход"]

    while True:
        print_slow(f"Доступные действия: {', '.join(commands)}")
        command = input("Ваш выбор: ").lower().strip()

        if command == commands[4]:
            return False
        elif command == commands[3]:
            show_inventory(inventory)
        elif command == commands[0]:
            print_slow("Вы прыгаете, но расстояние слишком велико. Вы падаете в воду и промокаете.")
        elif command == commands[1]:
            print_slow("Вы плывете, но вода холодная. Вы теряете силы.")
        elif command == commands[2]:
            if check_item(inventory, "лист") and check_item(inventory, "палка"):
                print_slow("Вы используете лист и палку, чтобы построить импровизированный мост!")
                print_slow("Вы перебираетесь через лужу и находите свою подругу!")
                return True
            else:
                print_slow("У вас нет нужных материалов для моста (нужны лист и палка).")
                print_slow("Вы понимаете, что это конец.")
                return False

        else:
            print_slow("Неизвестная команда.")


def level_four(inventory):
    print_slow("\nУРОВЕНЬ 4: Возвращение домой")
    print_slow("Вы спасли подругу, но путь домой полон опасностей.")
    print_slow("На пути стоит огромный камень. Его нужно как-то сдвинуть.")

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        print_slow(f"Попытка {attempts + 1} из {max_attempts}.")
        print_slow("Что вы сделаете? (толкнуть, обойти, использовать палку, инвентарь, выход)")

        command = input("Ваш выбор: ").lower().strip()

        if command == "выход":
            return False
        elif command == "инвентарь":
            show_inventory(inventory)
        elif command == "толкнуть":
            print_slow("Вы толкаете камень, но он слишком тяжелый. Вы тратите силы.")
            attempts += 1
        elif command == "обойти":
            print_slow("Вы пытаетесь обойти камень, но там обрыв. Придется возвращаться.")
            attempts += 1
        elif command == "использовать палку":
            if check_item(inventory, "палка"):
                print_slow("Вы используете палку как рычаг и сдвигаете камень!")
                print_slow("Путь свободен. Вы идете домой.")
                return True
            else:
                print_slow("У вас нет палки.")
                attempts += 1
        else:
            print_slow("Неизвестная команда.")
            attempts += 1

    print_slow("У вас закончились силы. Вы не смогли сдвинуть камень.")
    return False


def start_game():
    print_slow("Добро пожаловать в мир Webbed!")
    print_slow("Вы — маленький паучок, который хочет спасти свою подругу.")

    inventory = []

    if not level_one(inventory):
        print("Вы проиграли на первом уровне.")
        return

    if not level_two(inventory):
        print("Вы проиграли на втором уровне.")
        return

    if not level_three(inventory):
        print("Вы проиграли на третьем уровне.")
        return

    if not level_four(inventory):
        print("Вы проиграли на четвертом уровне.")
        return

    print_slow("\nСпасибо за игру! Вы настоящий герой!")


if __name__ == "__main__":
    start_game()