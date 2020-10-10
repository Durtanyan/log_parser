# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:23:37 2020

@author: lukin
"""

"""
Задача: 
1. распарсить log построчно в красивую таблицу.
2. сохранить в файл с расширением .txt

"""

log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

#Парсим строку в лист листов через .split(). Сначала по переносу строки ('\n'), затем по (';') 
#используем ListComprehension
list_string = [string.split(';') for string in [string for string in log.split('\n')]]

#т.к. все элементы нашего лога имеют 
#одинаковое строение, то распарсиваем
#первый элемент списка в словарь по
#ключам которого сформируем
#заголовки таблицы, в которую будем
#распарсивать в дальнейшем данные

dict_header = dict()
string = list_string[0]
for element in string:
	dict_key_value = element.split(':')
	dict_header[dict_key_value[0]] = dict_key_value[1]
	
#создаем переменные для заголовков таблицы
header_name = ""
header_gender = ""
header_item = ""
header_item_cost = ""

#формируем заголовки таблицы
for key in dict_header.keys():
	if key == "name":
		header_name = "Имя"
	elif key == "gender":
		header_gender = "Пол"
	elif key == "item":
		header_item = "Наименование"
	elif key == "item_cost":
		header_item_cost = "Цена"
		
#формируем красивый заголовок в рамке 
#для вывода к консоль и для записи в файл
print(" " + "_" * 61 + "")
print(f"| {header_name:10} | {header_gender:10} | {header_item:20} |  {header_item_cost:10}|")
print("|" + "-" * 61 + "|")

#создаем словарь из строки списка
#формируем построчно таблицу. #заполняем ее значениями словаря.
values_table_rows = dict()
for string in list_string:
	for element in string:
		dict_k_v = element.split(":")
		values_table_rows[dict_k_v[0]] = dict_k_v[1]
	print(" " + "_" * 61 + "")
	print(f"| {values_table_rows['name']:10} | {values_table_rows['gender']:10} | {values_table_rows['item']:20} |  {values_table_rows['item_cost']:9} |")

print("|" + "-" * 61 + "|")

