from tkinter import *
import math

foablak = Tk()
foablak.title("Henger")

def szamitas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a*a*math.pi*b
    d = 7.874*c
    e = 0.68*c
    mezo3.delete(0, END)
    mezo3.insert(0, f"{str(round(c, 2))} cm3")
    mezo4.delete(0, END)
    mezo4.insert(0, f"{str(round(d, 2))} g")
    mezo5.delete(0, END)
    mezo5.insert(0, f"{str(round(e, 2))} g")

cimke1=Label(foablak, text="Sugár (cm):")
cimke1.grid(row=1, column=0)
cimke2=Label(foablak, text="Magasság (cm):")
cimke2.grid(row=2, column=0)
cimke3=Label(foablak, text="Térfogat:")
cimke3.grid(row=4, column=0)
cimke4=Label(foablak, text="Vashenger:")
cimke4.grid(row=5, column=0)
cimke5=Label(foablak, text="Fahenger:")
cimke5.grid(row=6, column=0)

mezo1=Entry(foablak)
mezo1.grid(row=1, column=1, columnspan=1)
mezo2=Entry(foablak)
mezo2.grid(row=2, column=1, columnspan=1)
gomb4=Button(foablak, text="Kiszámít", command=szamitas)
gomb4.grid(row=3, column=2)
mezo3=Entry(foablak)
mezo3.grid(row=4, column=1, columnspan=1)
mezo4=Entry(foablak)
mezo4.grid(row=5, column=1, columnspan=1)
mezo5=Entry(foablak)
mezo5.grid(row=6, column=1, columnspan=1)

foablak.mainloop()