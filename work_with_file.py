import csv
import json
from  pprint import pprint
# ПОЛУЧЕНИ CSV
# Получение и распаковкаданных
# with open('test_csv.csv') as file:
#     read_csv = csv.reader(file)
#     for row in read_csv:
#         print(row)

# получение данных
# file = open('test_csv.csv')
# read_csv2 = csv.reader(file)
# print(read_csv2)
# #Преобразование данных в список
# data_list = list(read_csv2)
# print(data_list)
#
# read_csv3 = csv.DictReader(file)
# print(read_csv3)
# for i in read_csv3:
#     print(i)
# file.close()

# СОЗДАНИЕ CSV
# import json
#
#
# def read_json(file_path, word_max_len=6, top_words_amt=10):
#     """
#     функция для чтения файла с новостями.
#     """
#     # Ваш алгоритм
#     with open(file_path, encoding = 'utf-8') as f:
#         json_data = json.load(f)
#
#
#
#
# if _name_ == '_main_':
#     print(read_json('newsafr.json'))
# data_for_csv = [['student', 'group', 'course'],
#                 ['Bella', '1', 'Python'],
#                 ['Dobbi', '2', 'Git'],
#                 ['Voland', '1', 'Python']]
# with open('test_csv_write.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     for row in data_for_csv:
#         writer.writerow(row)
# file = open('test_csv_write.csv', 'w', newline='')
# writer = csv.writer(file)
# writer.writerows(data_for_csv)
# for row in data_for_csv:
#     writer.writerow(row)
# file.close()


# СОЗДАНИЕ JSON
# data_for_json = {'course' : {'Python': 'in process',
#                              'Git': 'in process',
#                              'C++': 'finish'}}
#
# json_str = "'course' : {'Python': 'в процессе', 'Git': 'в процессе', 'Введение в программирование': 'завершен'}"
# with open('test_json.json', 'w') as file:
#     json.dump(data_for_json, file, ensure_ascii=False, indent=2)
#
# j_s = json.dumps(json_str, ensure_ascii=False)
# print(j_s)

# ПОЛУЧЕНИЕ ДАННЫХ ИЗ JSON
# with open('test_json.json', encoding='utf-8') as file:
#     json_data = json.load(file)
# print(json_data)

