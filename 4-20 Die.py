from random import *
from Tkinter import *

def dado4():
    dado4=choice(range(1,5))
    print dado4
def dado6():
    dado6=choice(range(1,7))
    print dado6
def dado8():
    dado8=choice(range(1,9))
    print dado8
def dado10():
    dado10=choice(range(1,11))
    print dado10
def dado12():
    dado12=choice(range(1,13))
    print dado12
def dado20():
    dado20=choice(range(1,21))
    print dado20
    
w = Tk()
a = Button(w, text ="Dado de 4",command=dado4)
a.pack()
b = Button(w, text ="Dado de 6",command=dado6)
b.pack()
c = Button(w, text ="Dado de 8",command=dado8)
c.pack()
d = Button(w, text ="Dado de 10",command=dado10)
d.pack()
e = Button(w, text ="Dado de 12",command=dado12)
e.pack()
g = Button(w, text ="Dado de 20",command=dado20)
g.pack()

w.mainloop()
