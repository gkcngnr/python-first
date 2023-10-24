from tkinter import *
import random
root = Tk()
root.title("Vampir Oyunu")
#root.geometry("315x300")
root.config(bg="#355C7D")


label1=Label(text="Oyuncu sayısı giriniz..", padx=5, pady=2, font="courier", fg="#C7D0D7",bg="#355C7D")
label1.grid(row=0, column=0, columnspan=4)

e1 = Entry(root, width=50, borderwidth=6)
e1.grid(row=1, column=0, columnspan=4, pady=5)


oyuncu = []
roller = []
label_list = []
def enter():

    num = int(e1.get())
    for i in range(num):
        l = Label(text="Oyuncu adı:", bg="#F8B195")
        l.grid(row=3+i, column=0, pady=2)
        e = Entry(root, width=38, borderwidth=2, bg="#F8B195")
        e.grid(row=3+i, column=1)
        oyuncu.append(e)
        label_list.append(l)
    for i in range(num):
        l2 = Label(text="   Rol giriniz:")
        l2.grid(row=4+num+i, column=0,  pady=2)
        e2 = Entry(root, width=38, borderwidth=2)
        e2.grid(row=4+num+i, column=1)
        roller.append(e2)
        label_list.append(l2)
    global matchButton
    matchButton = Button(root, text="Match", command=entry_control, bg="#C7D0D7",padx=5, pady=2)
    matchButton.grid(row=4+2*num, column=0, columnspan=1, pady=5)


    def on_enter_pressed2(event):
        entry_control()

    e2.bind('<Return>', on_enter_pressed2)

def reset():
    for entry in oyuncu:
        entry.destroy()
    for entry in roller:
        entry.destroy()
    for label in label_list:
        label.destroy()
    if "matchButton" in globals():
        matchButton.destroy()
    e1.delete(0,END)
    oyuncu.clear()
    roller.clear()
    label_list.clear()




def entry_control():

    if "sonuclabel" in globals():
        sonuclabel.destroy()

    global rol
    rol = []
    global  oyuncu_isim
    oyuncu_isim = []
    sonuc_text = ""
    for entry in oyuncu:
        if len(entry.get().split()) == 0:
            sonuc_text = "Bos Bırakılmaz"
            break
        elif entry.get() in oyuncu_isim:
            sonuc_text = "Aynı isim olamaz"
            break
        else:
            oyuncu_isim.append(entry.get())

    for entry in roller:
        if len(entry.get().split()) == 0:
            sonuc_text = "Bos Bırakılmaz"
            break
        else:
            rol = [entry.get() for entry in roller]
    if len(sonuc_text) > 0:
        global errorlabel
        if "errorlabel" in globals():
            errorlabel.destroy()
        errorlabel = Label(text=sonuc_text, fg="red")
        errorlabel.grid(row=6 + 2 * int(e1.get()), column=0, columnspan=2)
        label_list.append(errorlabel)
    else:
        if "errorlabel" in globals():
            errorlabel.destroy()
        result()

def result():

    if "errorlabel" in globals():
        for error in "errorlabel":
            errorlabel.destroy()

    sonuc_text=""
    sonuc = {}
    rastgele = len(oyuncu_isim) - 1
    while rastgele >= 0:
        indeks1 = random.randint(0, rastgele)
        indeks2 = random.randint(0, rastgele)
        sonuc[oyuncu_isim[indeks1]] = rol[indeks2]
        oyuncu_isim.remove(oyuncu_isim[indeks1])
        rol.remove(rol[indeks2])
        rastgele -= 1

    for key,value in sonuc.items():
        sonuc_text += key.capitalize()
        sonuc_text += "-"
        sonuc_text += value.capitalize()
        sonuc_text += "\n"

    global sonuclabel
    sonuclabel =Label(text=sonuc_text, pady=5)
    sonuclabel.grid(row=5+2*int(e1.get()), column=0, columnspan=2)
    label_list.append(sonuclabel)


def on_enter_pressed1(event):
    enter()
e1.bind('<Return>', on_enter_pressed1)


b1=Button(root, text="Enter", command=enter, bg="#C7D0D7", padx=5, pady=2)
b1.grid(row=2, column=0, columnspan=1, pady=5)

resetButton = Button(root, text="Reset", command=reset, bg="#F67280", padx=5, pady=2)
resetButton.grid(row=2, column=1, columnspan=1, pady=5, padx=5)


root.mainloop()