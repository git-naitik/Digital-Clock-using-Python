from tkinter import *
import time as tk
clock=Tk()
clock.title("Digital Clock")
clock.geometry("600x50")

def time():
    d=tk.strftime("Date : %d-%m-%Y , Time : %H:%M:%S %p")
    l.config(text=d)
    l.after(1000,time)

l=Label(clock,bg="black",fg="red",font=('Arial',25,'bold'))
l.pack(anchor='center')
time()

mainloop()
