import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
#Creating tkinter object
prompt = tk.Tk()
prompt.title('Calculator')
prompt.resizable(0, 0)
frame = tk.Frame(master=prompt, bg="white", padx=10, pady=5)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=45)
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=5)
#defining myclick function which inserts the clicked number in frame
def myclick(number):
	entry.insert(tk.END, number)
#defining equal function which will perform the arithmetic operations and throw the resukt in frame
def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Syntax Error")
#defining a function which will delete the last entered digit in frame
def delete_last_digit():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])
#defining clear function which will delete all the numbers present in the frame
def clear():
	entry.delete(0, tk.END)

#Creating a button for each number and operator
button_1 = tk.Button(master=frame, text='1',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(1), font=(9))
button_1.grid(row=4, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(2), font=(9))
button_2.grid(row=4, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(3), font=(9))
button_3.grid(row=4, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(4), font=(9))
button_4.grid(row=3, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(5), font=(9))
button_5.grid(row=3, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(6), font=(9))
button_6.grid(row=3, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(7), font=(9))
button_7.grid(row=2, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(8), font=(9))
button_8.grid(row=2, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(9), font=(9))
button_9.grid(row=2, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0',bg="gray", padx=15, pady=10, width=3, command=lambda: myclick(0), font=(9))
button_0.grid(row=5, column=1, pady=2, padx=2)

button_add = tk.Button(master=frame, text="+",bg="darkgray", padx=15, pady=10, width=3, command=lambda: myclick('+'), font=(9))
button_add.grid(row=4, column=3, pady=2)

button_subtract = tk.Button(master=frame, text="-",bg="darkgray", padx=15, pady=10, width=3, command=lambda: myclick('-'), font=(9))
button_subtract.grid(row=3, column=3, pady=2)

button_multiply = tk.Button(master=frame, text="*",bg="darkgray", padx=15, pady=10, width=3, command=lambda: myclick('*'), font=(9))
button_multiply.grid(row=2, column=3, pady=2)

button_div = tk.Button(master=frame, text="/",bg="darkgray", padx=15, pady=10, width=3, command=lambda: myclick('/'), font=(9))
button_div.grid(row=1, column=3, pady=2)

button_point = tk.Button(master=frame, text=".",bg="gray", padx=15, pady=10, width=3, command=lambda: myclick('.'), font=(9))
button_point.grid(row=5, column=0, pady=2)

button_clear = tk.Button(master=frame, text="clear",bg="darkgray", padx=14, pady=10, width=11, command=clear, font=(9))
button_clear.grid(row=1, column=1, columnspan=2, pady=2)

button_del = tk.Button(master=frame, text="⇽", padx=15,bg="lightgray", pady=10, width=3, command=delete_last_digit, font=(9))
button_del.grid(row=1, column=0, pady=2)

button_equal = tk.Button(master=frame, text="=",bg="skyblue", padx=18, pady=10, width=10, command=equal, font=(9))
button_equal.grid(row=5, column=2, columnspan=2, pady=2)

prompt.mainloop()
