# -*- coding: utf-8 -*-
# author:BerryHN
import Tkinter as tk

top=tk.Tk()
listb=tk.Listbox(top)
listb2=tk.Listbox(top)
li=["c","python","php","html","sql","java"]
movie=["csss","jquery","bootstrap"]
for item in li:
    listb.insert(0,item)
for item in movie:
    listb2.insert(0,item)

listb.pack()
listb2.pack()
top.mainloop()

