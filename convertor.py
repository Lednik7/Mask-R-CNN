import os
from PIL import Image
name = input("Введите название новой папки: ")

dir = input("Введите дерикторию: ")

path = os.path.join(os.getcwd(), dir)

path2 = os.path.join(path, name)

try:
    os.mkdir(path2)
    print("Папка создана")
except:
    print("Папка уже создана")
             
for filename in os.listdir(path):
    if filename != name:
        try:
            img = Image.open(os.path.join(path, filename))
            img.save(os.path.join(path2, filename + ".jpg"))
        except PermissionError:
            print("Ошибка. Возможно в каталоге есть папка: " + filename)

print("Good")
