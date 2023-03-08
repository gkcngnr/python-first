from tkinter import *

root = Tk()
root.title("Calculator")

entry = Entry(root, width=38, borderwidth= 8)

entry.grid(row=0, column=0, columnspan=4)


def click(number):
    num = entry.get()
    entry.delete(0, END)
    entry.insert(0, num + str(number))
def add():
    entry.insert(END, "+")
    global operator
    operator = "+"
def subt():
    entry.insert(END, "-")
    global operator
    operator = "-"
def div():
    entry.insert(END, "/")
    global operator
    operator = "/"
def mult():
    entry.insert(END, "*")
    global operator
    operator = "*"
def clear():
    entry.delete(0, END)
def calc():
    first_number = entry.get().split(operator)[0]
    second_number = entry.get().split(operator)[1]
    if operator == "+":
        total = float(first_number) + float(second_number)
    elif operator == "-":
        total = float(first_number) - float(second_number)
    elif operator == "*":
        total = float(first_number) * float(second_number)
    elif operator == "/":
        total = float(first_number) / float(second_number)
    entry.delete(0, END)
    entry.insert(0, total)

#BUTTON FUNCTIONS
buttonadd = Button(root, text="+", padx=19, pady=10, command=add, bg="#C7D0D7", borderwidth=5)
buttonsub = Button(root, text="-", padx=20.5, pady=10, command=subt, bg="#C7D0D7", borderwidth=5)
buttondiv = Button(root, text="/", padx=21, pady=10, command=div ,bg="#C7D0D7",borderwidth=5)
buttonmult = Button(root, text="*", padx=20.5, pady=10, command=mult, bg="#C7D0D7",borderwidth=5)
buttonclear = Button(root, text="C", padx=20, pady=10, command=clear, bg="#C7D0D7",borderwidth=5)
button0 = Button(root, text="0", padx=49, pady=10, command= lambda: click(0))
button1 = Button(root, text="1", padx=20, pady=10, command= lambda: click(1))
button2 = Button(root, text="2", padx=20, pady=10, command= lambda: click(2))
button3 = Button(root, text="3", padx=20, pady=10, command= lambda: click(3))
button4 = Button(root, text="4", padx=20, pady=10, command= lambda: click(4))
button5 = Button(root, text="5", padx=20, pady=10, command= lambda: click(5))
button6 = Button(root, text="6", padx=20, pady=10, command= lambda: click(6))
button7 = Button(root, text="7", padx=20, pady=10, command= lambda: click(7))
button8 = Button(root, text="8", padx=20, pady=10, command= lambda: click(8))
button9 = Button(root, text="9", padx=20, pady=10, command= lambda: click(9))
buttondot = Button(root, text=".", padx=21, pady=10, command= lambda: click("."))
b_eq = Button(root, text="=", command=calc, width=2, bg="#C7D0D7",padx=18, pady=55, borderwidth=5)


#BUTTON POSITIONS
buttonadd.grid(row=1, column=0)
buttonsub.grid(row=1, column=1)
buttonmult.grid(row=1, column=2)
buttondiv.grid(row=1, column=3)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
buttonclear.grid(row=2, column=3)
b_eq.grid(row=3, rowspan=3, column=3)
button0.grid(row=5, column=0, columnspan=2)
buttondot.grid(row=5, column=2)



root.mainloop()