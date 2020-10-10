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

#подготавливаем данные для записи
#вводим имя файла, расширение и открываем файл
#файл открыт в режиме 'w' т.е. для для чтения и записи
name_file = input("Введите имя файла, в который будем записывать данные таблицы: ")
name_extension = name_file + ".txt"
opening_the_file_for_recording = open(name_extension, "w")

#Парсим строку в лист листов через .split(). 
#Сначала по переносу строки ('\n'),затем по (';') 
#используем ListComprehension
list_string = [string.split(';') for string in [string for string in log.split('\n')]]

#т.к. все элементы нашего лога имеют 
#одинаковое строение, то распарсиваем
#первый элемент списка в словарь по
#ключам которого сформируем
#заголовки таблицы, в которую будем
#распарсивать в дальнейшем данные
#используем DictComprehension
string = list_string[0]
dict_header = {element.split(':')[0]:element.split(':')[1] for element in string}
	
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
#для вывода к консоль
print(" " + "_" * 61 + "")
print(f"| {header_name:10} | {header_gender:10} |\
 {header_item:20} |  {header_item_cost:10}|")
print("|" + "-" * 61 + "|")

#для записи в файл
opening_the_file_for_recording.write(" " + "_" * 60 + "" + "\n")
opening_the_file_for_recording.write("|" + f"{header_name:10}" + "|" + f"{header_gender:10}"\
+ "|" + f"{header_item:26}" + "|" + f"{header_item_cost:11}" + "|"+ "\n")
opening_the_file_for_recording.write("|" + "_" * 60 + "|" + "\n")

#создаем словарь из строки списка
#формируем построчно таблицу. 
#заполняем ее значениями словаря.
values_table_rows = dict()
for string in list_string:
	for element in string:
		dict_k_v = element.split(":")
		values_table_rows[dict_k_v[0]] = dict_k_v[1]
    #выводим в консоль
	print(" " + "_" * 61 + "") 
	print(f"| {values_table_rows['name']:10} | {values_table_rows['gender']:10} |\
 {values_table_rows['item']:20} |  {values_table_rows['item_cost']:9} |")
    #записываем в файл
	opening_the_file_for_recording.write(" " + "_" * 61 + ""+ "\n") 
	opening_the_file_for_recording.write("|" + f"{values_table_rows['name']:10}" + "|" +\
f"{values_table_rows['gender']:10}" + "|" + f"{values_table_rows['item']:26}" + "|" + \
f"  {values_table_rows['item_cost']:9}" + "|"+ "\n")

#выводим в консоль
print("|" + "-" * 61 + "|")
#записываем в файл
opening_the_file_for_recording.write(" " + "-" * 61 + ""+ "\n")
#закрываем записанный файл
print(f'Записан файл {name_extension}')
opening_the_file_for_recording.close()
#проверка закрытия файла
closed_file = opening_the_file_for_recording.closed
if closed_file:
    print("Файл закрыт.")
else:
    print("Вы забыли закрыть файл!")
