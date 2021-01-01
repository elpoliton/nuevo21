# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 22:03:39 2020

@author: JOSE
"""
import time
from turtle import *
import random
from tkinter import*
from playsound import playsound
playsound('anionuevosong.mp3',block=False)
window=Tk()
window.configure(bd=10)

def convert():
    display["text"] = combo.get()
window.geometry("800x900")
window.title("Primera Ventana")
window.config(bg="gold")
window.title("FELIZ AÑO NUEVO")


canvas = Canvas(window, width=770, height=850)
canvas.grid(column=0, row=14, columnspan=2)

pantalla = TurtleScreen(canvas)
pantalla.bgcolor("gold")
pantalla.colormode(255) #setting the screen color-mode
t = RawTurtle(pantalla)

t.begin_fill()
t.pen(fillcolor="red",pensize=8,speed=10)

#COUNTDOWN
num = int(10)
numx = int(num)
nums=int(num)
nume=0
t.hideturtle()
while not int(nume)==int(nums):
    t.clear()
    t.write(int(numx),font=("Fixedsys",48,"normal"))
    numx=int(numx)-1
    nume+=1
    time.sleep(1)
t.clear()
numx=0

#FIREWORK
t.speed(300)#100
for i in range(10):
    x =random.randint(-250,250)
    y =random.randint(-250,250)
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    size = random.randint(10,200)
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    t.color(r,g,b)
    
    for i in range(36):
        t.fd(size)
        t.bk(size)
        t.lt(10)

t.clear()
pantalla.bgcolor("gold")

t.pen(pencolor="red",fillcolor="red",pensize=2,speed=1)

t.penup()
t.goto(0,0)
t.pendown()

t.pen(pencolor="black",fillcolor="black",pensize=2,speed=1)
style = ("bold",50,"italic") 
t.write("¡FELIZ AÑO NUEVO!",font=style,align="center")
t.penup()
t.rt(90)
t.fd(100)
t.pendown()
style = ("bold",20) 
t.write("Muchos éxitos en todos los proyectos que se propongan" ,font=style,align="center")
t.penup()
t.fd(30)
t.pendown()
t.write("y para los que estamos con la tesis, es hora de terminarla :D" ,font=style,align="center")
t.penup()
t.fd(80)
t.pendown()
style = ("bold",15)
t.write("Les desea Jose Guzmán" ,font=style,align="center")
t.penup()
t.bk(400)
t.pendown()
style = ("bold",150)
t.write("2021" ,font=style,align="center")

t.up()
t.fd(50)
t.speed(80)
list1=["purple", "red","orange", "blue", "green"]
t.pendown()
for i in range(50):#200
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.fd(i)
    t.lt(59)

#window.minsize(100 , 100)
#window.maxsize(1500, 1500)
canvas.pack()
my_image=PhotoImage(file='tesis.gif')
canvas.create_image(0,0,anchor=CENTER,image=my_image)#anchor=NW

window.mainloop()
