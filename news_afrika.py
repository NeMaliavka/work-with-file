import json
from collections import Counter
import xml.etree.ElementTree as ET

# with open('newsafr.json', encoding="utf8") as file:
#     json_data = json.load(file)
#
# news = json_data['rss']['channel']['items']
# print(news)
# print(type(news))
# words = []
# for row in news:
#     word_list = row['description'].split()
#     for word in word_list:
#         if len(word) > 6:
#             words.append(word)
# print(words)

# words_counter = Counter(words)
# print(words_counter)
# top_10 = [w[0] for w in words_counter.most_common(10)]
# print(top_10)
# print(json_data)
# print(type(json_data))



# -----import json
#
#


#-------Чтение json файла и получение нужной информации
# Вам дан xml-файл с новостями. Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов.
#
# Приведение к нижнему регистру не требуется.
#
# В результате корректного выполнения задания будет выведен следующий результат:
# ['туристов', 'компании', 'Wilderness', 'странах', 'туризма', 'которые', 'африканских', 'туристы', 'является', 'природы']
# def read_json(file_path, word_max_len=6, top_words_amt=10):
#     """
#     функция для чтения файла с новостями.
#     """
#     with open(file_path, encoding="utf8") as file:
#         json_data = json.load(file)
#     news = json_data['rss']['channel']['items']
#     # print(news)
#     # print(type(news))
#     words = []
#     for row in news:
#         word_list = row['description'].split()
#         for word in word_list:
#             if len(word) > word_max_len:
#                 words.append(word)
#     words_counter = Counter(words)
#     top_10 = [w[0] for w in words_counter.most_common(top_words_amt)]
#     return top_10
#
#
# if __name__ == '__main__':
#     print(read_json('newsafr.json'))





# -------- xml
# parser = ET.XMLParser(encoding='utf-8')
# tree = ET.parse('newsafr.xml', parser)
# root = tree.getroot()
# print(root.tag)
# print(root.text)
# print(root.attrib)
#
# news = root.findall('channel/item')
# print(len(news))
#
# for row in news:
#     title = row.find('title')
#     print(title.text)




import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_path, parser)
    root = tree.getroot()

    news = root.findall('channel/item')
    words = []
    for row in news:
        description = row.find('description')
        word_list = description.text.split()
        for word in word_list:
            if len(word) > word_max_len:
                words.append(word)
    words_counter = Counter(words)
    top_10 = [w[0] for w in words_counter.most_common(top_words_amt)]
    return top_10


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))
