import os
import time
from pprint import pprint
import json

cook_data = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

# with open("book_cook.txt", 'w') as f:
# val={}
# for key, value in cook_data.items():
#   f.write(key)
#  f.write('\n%s\n'%str(len(value)))
# for val in value:
#    for key, value in val.items():
#       f.write('%s|'%str(value))
#  f.write('\n')
# f.write('\n')
file_path = "book_cook.txt"

def make_cook_book("book_cook.txt"):
    Kok = {}
    with open("book_cook.txt", encoding='UTF-8') as file:
        for

def r_bk():
    f_path = os.path.join(os.getcwd(), "book_cook.txt")
    c_b = {}
    with open(f_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                for key, value in ingrs.items():
                    ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                    ing_list.appened(ingrs.item())
                f.readline()
                c_b[dish_name] = ing_list
    return c_b

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:
        if dish_name in c_b:
            for ings in c_b[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list