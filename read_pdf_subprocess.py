import subprocess

# Замените 'yourfile.pdf' на путь к вашему PDF файлу
pdf_file_path = r'tinkoff.pdf'

# Формирование команды для выполнения
command = ['pdftotext', pdf_file_path, '-']

# Запуск команды и получение результата
try:
    result = subprocess.run(command, check=True, text=True)
    # Вывод результата выполнения команды
    print(result.stdout)
except subprocess.CalledProcessError as e:
    # Если произошла ошибка при выполнении команды, выводим информацию об ошибке
    print(f"Ошибка при выполнении команды: {e.stderr}")
