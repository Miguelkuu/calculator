from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Button(frm, text="AC").grid(column=0, row=0)
ttk.Button(frm, text="+/-").grid(column=1, row=0)
ttk.Button(frm, text="%").grid(column=2, row=0)
ttk.Button(frm, text="/").grid(column=3, row=0)
ttk.Button(frm, text="7").grid(column=0, row=1)
ttk.Button(frm, text="8").grid(column=1, row=1)
ttk.Button(frm, text="9").grid(column=2, row=1)
ttk.Button(frm, text="*").grid(column=3, row=1)
ttk.Button(frm, text="4").grid(column=0, row=2)
ttk.Button(frm, text="5").grid(column=1, row=2)
ttk.Button(frm, text="6").grid(column=2, row=2)
ttk.Button(frm, text="-").grid(column=3, row=2)
ttk.Button(frm, text="1").grid(column=0, row=3)
ttk.Button(frm, text="2").grid(column=1, row=3)
ttk.Button(frm, text="3").grid(column=2, row=3)
ttk.Button(frm, text="+").grid(column=3, row=3)
ttk.Button(frm, text="0").grid(row=4, column=0, columnspan=2, sticky="we")
ttk.Button(frm, text=".").grid(column=2, row=4)
ttk.Button(frm, text="=").grid(column=3, row=4)

root.mainloop()