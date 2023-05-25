from tkinter import *
from PIL import ImageTk,Image

dastur = Tk()
dastur.geometry("1366x768")
dastur.configure(bg="#e9edc9")
dastur.title("Urganch")
dastur.iconbitmap("bank (1).ico")
Frame(dastur,height=2,width=1366,bg="black").place(x=0,y=0)
Frame(dastur,height=2,width=1366,bg="black").place(x=0,y=70)
image_bg = PhotoImage(file="accounts.png")
Label(dastur, image=image_bg, bg="#e9edc9").place(x=700, y=100)


def Kirim():
    top = Toplevel()
    top.title("Kirim")
    top.geometry("700x200+300+300")
    top.resizable(FALSE,FALSE)
    top.iconbitmap("bank (1).ico")
    top.configure(bg="#e9edc9")
    Label(top, text="summa:").place(x=20, y=140)
    som_ent = IntVar()
    Entry(top, textvariable=som_ent, width=10).place(x=70,y=140)
    Label(top, text="dollar:").place(x=140, y=140)
    usa_ent = IntVar()
    Entry(top, textvariable=usa_ent, width=10).place(x=180, y=140)
    Label(top, text="jami:").place(x=250, y=140)
    overall = int(som_ent)+int(usa_ent)*11300                        #<= wo'rina galib qoldim
    Entry(top, textvariable=overall, width=10).place(x=280, y=140)

Menyu = Menu()

dastur.config(menu=Menyu, bg="#e9edc9")
fayl = Menu(Menyu, tearoff=0, bg='#e9edc9')
Menyu.add_cascade(label= 'Tovar aylanma', menu=fayl)
fayl.add_cascade(label='Kirim', activebackground='#d5bdaf', activeforeground='black', command=Kirim)
fayl.add_separator()
fayl.add_cascade(label='Nasiya savdo', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Naqd savdo', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()



dastur.config(menu=Menyu, bg="#e9edc9")
fayl = Menu(Menyu, tearoff=0, bg='#e9edc9')
Menyu.add_cascade(label= 'Pul aylanma',menu=fayl)
fayl.add_cascade(label='Kirim', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Chiqim', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Valyuta ayirboshlash', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()



dastur.config(menu=Menyu, bg="#e9edc9")
fayl = Menu(Menyu, tearoff=0, bg='#e9edc9')
Menyu.add_cascade(label= 'Ma\'lumotlar',menu=fayl)
fayl.add_cascade(label='Pul hisobi', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Tovar oborot', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Omborxona hisoboti', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Kassa hisoboti', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()


dastur.config(menu=Menyu, bg="#e9edc9")
fayl = Menu(Menyu, tearoff=0, bg='#e9edc9')
Menyu.add_cascade(label= 'Foyda',menu=fayl)
fayl.add_cascade(label='Mijozlar bo\'yicha', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Tovarlar bo\'yicha', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Valyuta bo\'yicha', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()


dastur.config(menu=Menyu, bg="#e9edc9")
fayl = Menu(Menyu, tearoff=0, bg='#e9edc9')
Menyu.add_cascade(label= 'Ustav kapital management',menu=fayl)
fayl.add_cascade(label='Pul qo\'shish', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Pul kamaytirish', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()
fayl.add_cascade(label='Kapitalni nollashtirish', activebackground='#d5bdaf', activeforeground='black')
fayl.add_separator()

dastur.mainloop()