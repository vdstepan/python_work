# Вывод каталога файлов с помощью os.walk до заданного уровня
# Функция walklevel(some_dir, level) позволяет в отлиции от walk посмотреть вглубь каталог some_dir только до уровня level

import os


def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]



for path, dirs, files in os.walk('.'):
    print (path, dirs, files)
    del dirs[:]


print("=============================")
print("Смотрим до 0-го уровня ")

for path, dirs, files in walklevel(".",0):
    print (path, dirs, files)


print("=============================")
print("Смотрим до 2-го уровня ")

for path, dirs, files in walklevel(".",2):
    print (path, dirs, files)    