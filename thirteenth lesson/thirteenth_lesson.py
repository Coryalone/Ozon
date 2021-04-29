import json
import os
from tkinter import *
from tkinter.messagebox  import *
from tkinter.filedialog import *


class Notepad():
    __root = Tk()
    __thisTextArea = Text(__root, font=('Verdana', 30))    
    __file = None
    def __init__(self, **kwargs):        
        self.__root.title('Тескстовый редактор')
        self.__root.geometry('500x500')        
        self.__thisTextArea.grid(sticky=N+E+S+W)        
        self.load = Button(text='Загрузить')
        self.load.bind('<Button-1>', self.__openFile)
        self.load.place(relx=.035, rely=.985, anchor="c", height=30, width=130)
        self.save = Button(text='Сохранить')
        self.save.bind('<Button-1>', self.__saveFile)
        self.save.place(relx=.965, rely=.985, anchor="c", height=30, width=130)    

    def __openFile(self, event):
        self.__file = askopenfilename()
        if self.__file == '':
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file))
            self.__thisTextArea.delete(1.0, END )
            file = open(self.__file, encoding="utf8")
            self.__thisTextArea.insert(1.0, file.read())
            file.close()           

    def __saveFile(self, event):
        if self.__file == None:
            self.__file = asksaveasfilename(defaultextension = '.txt')
            if self.__file == '':
                self.__file = None
            else:
                absolutename = os.path.abspath(self.__file)    
                with open('settings.json', 'w', encoding="utf8") as f:
                    f.write(json.dumps({'file_name': absolutename}))
                file = open(self.__file, 'w', encoding="utf8")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + 'Блокнот')
        else:
            absolutename = os.path.abspath(self.__file)    
            with open('settings.json', 'w', encoding="utf8") as f:
                f.write(json.dumps({'file_name': absolutename}))
            file = open(self.__file, 'w', encoding="utf8")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def run(self):
        link = os.path.abspath('settings.json')
        if (os.path.exists('settings.json')):
            with open('settings.json', 'r') as f:
                data = json.load(f)                
                absolutename = data['file_name']                
            if (os.path.exists(absolutename)):
                file = open(absolutename, encoding="utf8")            
                self.__thisTextArea.insert(1.0, file.read())
                file.close()
        self.__root.mainloop()

notepad = Notepad()
notepad.run()