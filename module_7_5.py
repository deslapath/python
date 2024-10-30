import os

import time

directory = r'C:\Users\existe\PycharmProjects\Homeworks'

for root, dirs, files in os.walk(directory):
    for file in files:
     filepath = os.path. join(directory)
file_size = os.path.getsize(directory)
file_time = os.path.getatime(directory)
file_time_formatted = time. strftime('%Y-%m-%d %H : %M: %S ', time.localtime(file_time))
parent_dir = os.path.dirname(filepath)

print(f'Обнаружен файл: {filepath}')
print(f"Размер: {file_size} bytes")
print(f"Время изменения: {file_time_formatted}")
print(f"Родительская директория: {parent_dir}")
