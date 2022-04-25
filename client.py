from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from urllib import request, parse
tk = Tk()
tk2 = None
tk.geometry("500x500")
tk.resizable(0, 0)
tk.title("Удаленное изменение и получение файлов")
cont = None
fnf = None
lbl_cont = None
but_save = None
def save2():
    global cont
    global but_save
    fn = fd.askopenfilename()
    f = open(fn, "w")
    f.write(cont)
    f.close()
    but_save.destroy()
def save():
    global tk
    global but_save
    but_save = Button(tk, command=save2, text="Сохранить в файл")
    but_save.pack()

def get2():
    global tk
    global tk2
    global cont
    global lbl_cont
    IP = "http://"+ip.get()+":"+port.get()
    fname = fnf.get()
    cont = str(request.urlopen(IP + "/get?file=" + fname).read(), 'utf-8')
    tk2.destroy()
    tk2 = None
    lbl_cont = Label(tk, text=cont)
    lbl_cont.pack()
    save()
def set_():
    IP = "http://"+ip.get()+":"+port.get()
    fn = fd.askopenfilename()
    f = open(fn)
    cont = f.read().replace(" ", "%20")
    f.close()
    name = fn.split("\\")[-1]
    val = {"file": name, "cont": cont}
    data = parse.urlencode(val)
    data = data.encode('utf-8')
    req = IP + "/set?" + str(data)
    try:
        request.urlopen(req)
        messagebox.showinfo("Загрузка файла", "Файл загружен успешно!")
    except:
        messagebox.showerror("Загрузка файла", "Произошла ошибка. Убедитесь, что правильно указан IP-адрес")
def get():
    global tk2
    global fnf
    tk2 = Tk()
    tk2.title("Получение файла")
    tk2.geometry("500x500")
    tk2.resizable(0, 0)
    lbl3 = Label(tk2, text="Имя файла: ")
    fnf = Entry(tk2, width=20)
    lbl3.pack()
    fnf.pack()
    getbut = Button(tk2, text="Получить", command=get2)
    getbut.pack()
    tk2.mainloop()
lbl1 = Label(tk, text="IP-адрес сервера: ")
lbl1.pack()
ip = Entry(tk, width=13)
ip.insert(0, "192.168.1.")
ip.pack()
lbl2 = Label(tk, text="Порт сервера: ")
lbl2.pack()
port = Entry(tk, width=4)
port.insert(0, "5000")
port.pack()
set_but = Button(tk, text="Загрузка файла на сервер", command=set_)
get_but = Button(tk, text="Получение файла с сервера", command=get)
set_but.pack()
get_but.pack()
tk.mainloop()
