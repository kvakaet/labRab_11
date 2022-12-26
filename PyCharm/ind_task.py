#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def exit_to_program():
    print('всего доброго')
    return exit(1)


def help_program():
    print("add - добавление рейса\n"
          "help - помощь по командам\n"
          "select \"пункт назначения\" - вывод самолетов летящих в п.н.\n"
          "exit - выход из программы")


def add_program(planes):
    plane = dict()
    plane["destination"] = input("Пункт назначения:\n")
    plane["flight_number"] = int(input("Номер рейса:\n"))
    plane["type_plane"] = input("Тип самолета\n")
    planes.append(plane)
    planes.sort(key=lambda key_plane: key_plane.get("flight_number"))
    return planes


def select_program(planes):
    lst = list(map(lambda x: x.get("destination"), planes))
    point = input('выберите нужное вам место\n')
    print("результаты поиска")
    if point in lst:
        print('рейсы в эту точку')
        for i in planes:
            if point == i["destination"]:
                print(f"{i['flight_number']}........{i['type_plane']}")
    else:
        print("рейсов не найдено")


def plane_print(planes):
    for i in planes:
        print(f"куда - {i['destination']} номер - {i['flight_number']} самолет - {i['type_plane']}")


def error():
    print('неверная комманда')


def menu(lst_plane):
    command = input('введите команду("help" - руководство по командам)\n>>>').lower()
    if command == 'exit':
        exit_to_program()
    elif command == 'help':
        help_program()
    elif command == 'add':
        lst_plane = add_program(lst_plane)
    elif command == 'select':
        select_program(lst_plane)
    elif command == 'plane_print':
        plane_print(lst_plane)
    else:
        error()


if __name__ == '__main__':
    lst_planes = list()

    while True:
        menu(lst_planes)
