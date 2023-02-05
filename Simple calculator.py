from tkinter import *
import numexpr as ne
root=Tk()

root.title("Simple Calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def myClick():
    return

def button_click(number):
    if number == "delete":
        e.delete(0, END)
    elif  number == "=":        
        total_val = ne.evaluate(e.get())
        e.delete(0, END)
        e.insert(0, total_val)
    else:
        current = e.get() + str(number)
        e.delete(0, END)
        e.insert(0, current)    

#Кнопки чисел
button_1 =Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+"))
button_min = Button(root, text="-", padx=40, pady=20, command=lambda: button_click("-"))
button_division = Button(root, text="/", padx=40, pady=20, command=lambda: button_click("/"))
button_multiplication = Button(root, text="*", padx=40, pady=20, command=lambda: button_click("*"))


button_equal= Button(root, text="=", padx=40, pady=20, command=lambda: button_click("="))
button_clear= Button(root, text="Clear", padx=80, pady=20, command=lambda: button_click("delete"))

#Кнопки вывести на экран
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)


button_add.grid(row=4, column=1)
button_min.grid(row=4, column=2)
button_division.grid(row=5, column=0)
button_multiplication.grid(row=5, column=1)

button_equal.grid(row=5, column=2)
button_clear.grid(row=6,  column=0, columnspan=2)

myButton = Button(root, text="Enter Your Stock Quote", command=myClick)

root.mainloop()