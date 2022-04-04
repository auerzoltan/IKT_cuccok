from tkinter import *
import math


foablak = Tk()
foablak.title("Henger folyadék")
gyoker = "H:\\IKT\\tkinter\\"



cimke1=Label(foablak, text="Sugár (cm):")
cimke1.grid(row=1, column=0)
cimke2=Label(foablak, text="Magasság (cm):")
cimke2.grid(row=2, column=0)
cimke3=Label(foablak, text="Mennyi liter borunk van?")
cimke3.grid(row=3, column=0)
cimke4=Label(foablak, text="Ennyi literes a hordó:")
cimke4.grid(row=5, column=0)
cimke5=Label(foablak, text="Belefér-e:")
cimke5.grid(row=6, column=0)
cimke6=Label(foablak, text="Mennyi férne még bele:")
cimke6.grid(row=7, column=0)
cimke7=Label(foablak, text="Telítettség százalékosan:")
cimke7.grid(row=8, column=0)

mezo1=Entry(foablak)
mezo1.grid(row=1, column=1, columnspan=1)
mezo2=Entry(foablak)
mezo2.grid(row=2, column=1, columnspan=1)
mezo3=Entry(foablak)
mezo3.grid(row=3, column=1, columnspan=1)
gomb4=Button(foablak, text="Kiszámít")
gomb4.grid(row=4, column=1, columnspan=1)
mezo5=Entry(foablak)
mezo5.grid(row=5, column=1, columnspan=1)
mezo6=Entry(foablak)
mezo6.grid(row=6, column=1, columnspan=1)
mezo7=Entry(foablak)
mezo7.grid(row=7, column=1, columnspan=1)
mezo8=Entry(foablak)
mezo8.grid(row=8, column=1, columnspan=1)

foablak.mainloop()