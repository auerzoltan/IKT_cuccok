from tkinter import *
ablak1 = Tk()
gyoker = "C:\\Users\\auerzoltan\\Desktop\\tkinter\\"
ablak1.geometry("450x450")
ablak1.title("IKT Tkinter")
icon = PhotoImage(file="szamologep.png")
ablak1.iconphoto(True, icon)
ablak1.config(background="black")
elsokep= PhotoImage(file=gyoker+"alma.png")

cimke = Label(ablak1, 
            text="Üdvözlet!", 
            fg="#553388",
            bg="yellow",
            font=("Arial", 45, "bold"),
            bd=10,
            relief=RAISED,
            padx=25,
            pady=30,
            image=elsokep,
            compound="center").pack()


ablak1.mainloop()