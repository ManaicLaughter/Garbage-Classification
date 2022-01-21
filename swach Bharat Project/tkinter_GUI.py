import cv2
import numpy as np
from tkinter import *
from namer import nameit
from garbage_recognition import *

w = Tk()

def one():
    liquid()
def two():
    hazardous()
def three():
    medical()
def four():
    ewaste()
def five():
    recycle()
def six():
    green()

width_of_window = 1080
height_of_window = 800
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1)


a = '#249794'
Frame(w, width=1080, height=800, bg=a).place(x=0, y=0)  # 249794
b1 = Button(w, width=20, height=2, text='Household Waste', command=one, border=0, fg=a, bg='white')
b1.place(x=820, y=172)

b2 = Button(w, width=20, height=2, text='Hazardous Waste', command=two, border=0, fg=a, bg='white')
b2.place(x=820, y=242)

b3 = Button(w, width=20, height=2, text='Medical Waste', command=three, border=0, fg=a, bg='white')
b3.place(x=820, y=312)

b4 = Button(w, width=20, height=2, text='E-Waste', command=four, border=0, fg=a, bg='white')
b4.place(x=820, y=382)

b5 = Button(w, width=20, height=2, text='Recyclable Waste', command=five, border=0, fg=a, bg='white')
b5.place(x=820, y=452)

b7 = Button(w, width=20, height=2, text='Green Waste', command=six, border=0, fg=a, bg='white')
b7.place(x=820, y=522)

button_exit= Button(w,width=8, height=1, text="Exit", command=w.destroy,border=2, fg='red', bg='white' )
button_exit.place(x=1015, y=5)

######## Label

l1 = Label(w, text='GARBAGE', fg='white', bg=a)
lst1 = ('Calibri (Body)', 30, 'bold', 'underline')
l1.config(font=lst1)
l1.place(x=310, y=50)

l2 = Label(w, text='Classifier', fg='white', bg=a)
lst2 = ('Calibri (Body)', 30, 'underline')
l2.config(font=lst2)
l2.place(x=530, y=52)

l3 = Label(w, text='Select the waste you want to recognize.', fg='black', bg=a)
lst3 = ('Arial', 22)
l3.config(font=lst3)
l3.place(x=50, y=120)

l4 = Label(w, text='1. LIQUID OR SOLID HOUSEHOLD WASTE ', fg='white', bg=a)
lst3 = ('Arial', 16)
l4.config(font=lst3)
l4.place(x=50, y=170)
l5 = Label(w, text='      Eg: Household wastewater, cooking oil, fats, grease etc. ', fg='white', bg=a)
lst3 = ('Calibri (Light)', 12)
l5.config(font=lst3)
l5.place(x=50, y=200)

l6 = Label(w, text='2. HAZARDOUS WASTE  ', fg='white', bg=a)
lst3 = ('Arial', 16)
l6.config(font=lst3)
l6.place(x=50, y=240)
l7 = Label(w, text='      Eg: Pesticides and other garden chemicals. Batteries, Deodrants etc . ', fg='white', bg=a)
lst3 = ('Calibri (Light)', 12)
l7.config(font=lst3)
l7.place(x=50, y=270)

l8 = Label(w, text='3. MEDICAL/CLINICAL WASTE  ', fg='white', bg=a)
lst3 = ('Arial', 16)
l8.config(font=lst3)
l8.place(x=50, y=310)
l9 = Label(w, text='      Eg: Used syringes and needles, used swabs, plasters and bandages etc. ', fg='white', bg=a)
lst3 = ('Calibri (Light)', 12)
l9.config(font=lst3)
l9.place(x=50, y=340)

l10 = Label(w, text='4. ELECTRICAL WASTE (E-WASTE)  ', fg='white', bg=a)
lst3 = ('Arial', 16)
l10.config(font=lst3)
l10.place(x=50, y=380)
l11 = Label(w, text='      Eg: TV appliances, computers, laptops, tablets, mobile phones, white goods etc. ', fg='white', bg=a)
lst3 = ('Calibri (Light)', 12)
l11.config(font=lst3)
l11.place(x=50, y=410)

l12 = Label(w, text='5. RECYCLABLE WASTE  ', fg='white', bg=a)
lst3 = ('Arial', 16)
l12.config(font=lst3)
l12.place(x=50, y=450)
l13 = Label(w, text='      Eg: Plastic, glass, paper, cardboard, metal, plastic, tires, textiles, batteries, and electronics etc. ', fg='white', bg=a)
lst3 = ('Calibri (Light)', 12)
l13.config(font=lst3)
l13.place(x=50, y=480)

l14 = Label(w, text='6. GREEN WASTE   ', fg='white', bg=a)
lst3 = ('Arial', 16)
l14.config(font=lst3)
l14.place(x=50, y=520)
l15 = Label(w, text='      Eg: Leaves, tree trimmings, branches, flowers, and other plant material etc. ', fg='white', bg=a)
lst3 = ('Calibri (Light)', 12)
l15.config(font=lst3)
l15.place(x=50, y=550)

w.mainloop()