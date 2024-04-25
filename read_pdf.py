import PyPDF2

pdf_file = open('sber.pdf', 'rb')  # Открываем файл в режиме чтения бинарных данных

pdf_reader = PyPDF2.PdfReader(pdf_file)  # Создаем объект PdfFileReader
print(pdf_reader)
num_pages = len(pdf_reader.pages)  # Получаем количество страниц в файле
print(num_pages)

for page in range(num_pages):
    pdf_page = pdf_reader.pages[page]  # Получаем страницу
    print(pdf_page.extract_text())  # Выводим текст страницы
 
pdf_file.close()  # Закрываем файл

