from tkinter import*
from tkinter import ttk



def on_button_click(value):
    current = entry_var.get()
    if value == "C":
        entry_var.set("")
    elif value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(current + str(value))








root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
entry_var = StringVar()
ttk.Entry(frm, textvariable=entry_var).grid(column=0, row=0, columnspan = 5)





ttk.Button (frm, text="1", command=lambda : on_button_click("1")).grid(column=0, row=3)

ttk.Button(frm, text="2", command=lambda : on_button_click("2")).grid(column=1, row=3)
                                                    
ttk.Button(frm, text="3", command=lambda : on_button_click("3")).grid(column=2, row=3)

ttk.Button(frm, text="4", command=lambda: on_button_click("4")) .grid(column=0, row=2)

ttk.Button(frm, text="5", command=lambda : on_button_click("5")) .grid(column=1, row=2)


ttk.Button(frm, text="6", command=lambda : on_button_click("6")) .grid(column=2, row=2)

ttk.Button(frm, text="7", command=lambda : on_button_click("7")) .grid(column=0, row=1)

ttk.Button(frm, text="8", command=lambda: on_button_click("8")) .grid(column=1, row=1)

ttk.Button(frm, text="9", command=lambda: on_button_click("9")) .grid(column=2, row=1)

ttk.Button(frm, text="0", command=lambda: on_button_click("0")) .grid(column=1, row=4)
ttk.Button(frm, text=".", command=lambda: on_button_click(".")) .grid(column=2, row=4)
ttk.Button(frm, text="=", command=lambda: on_button_click("=")) .grid(column=0, row=4)

ttk.Button(frm, text="+", command=lambda: on_button_click("+")) .grid(column=4, row=3)
ttk.Button(frm, text="-", command=lambda: on_button_click("-")) .grid(column=4, row=2)
ttk.Button(frm, text="*", command=lambda: on_button_click("*")) .grid(column=4, row=1)
ttk.Button(frm, text="/", command=lambda: on_button_click("/")) .grid(column=4, row=4)
root.mainloop()
