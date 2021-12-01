import pathlib
import os
from tkinter import *


# print("--------------")

# получаем текущий каталог и удаляем \python выходим на уровень выше
currentDir = os.getcwd()
currentDir = currentDir[:-6]
currentDir = currentDir.rstrip(os.path.sep)

# print(currentDir)
# print("--------------")


# получаем список файлов и каталогов
example_dir = currentDir
dir = pathlib.Path(example_dir)
files = [file.name for file in dir.iterdir() if file.is_file()]
subdirs = [file.name for file in dir.iterdir() if file.is_dir()]

# print(subdirs)
# print("--------------")
# print(files)

# for i in range(len(subdirs)):
#   print(subdirs[i])

print(len(subdirs))

window = Tk()

wrapper1 = LabelFrame(window)
wrapper2 = LabelFrame(window)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = Scrollbar(wrapper1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda event : mycanvas.configure(scrollregion = mycanvas.bbox('all')))


myframe = Frame(mycanvas)

mycanvas.create_window((0,0), window=myframe, anchor="nw")


wrapper1.pack(fill="both",  expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both",  expand="yes", padx=10, pady=10)


class CheckButton:
  def __init__(self, master, title):
    self.var = BooleanVar()
    self.var.set(0)
    self.title = title
    self.cb = Checkbutton(master, text=title, variable=self.var, onvalue=1, offvalue=0)
    self.cb.pack(anchor=W)


check = []

for i in range(len(subdirs)):
  check.append(CheckButton(myframe, subdirs[i]))



window.geometry("500x500")
window.resizable(False, False)
window.title("Файлы")
window.mainloop()






