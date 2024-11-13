#!/usr/bin/env python
# coding: utf-8

# In[7]:


from tkinter import *
import math

root = Tk()

canvas = Canvas(root, width=600, height=600)
canvas.pack()

canvas.create_oval(100, 100, 500, 500)
point = canvas.create_oval(295, 295, 305, 305, fill="red")

def change():
    global direction
    direction = -direction
    
b = Button(text='Изменить направление', width=15, height=15)
b.config(command=change)
b.pack()

def move_point():
    global angle, direction, speed
    x = int(300 + 200 * math.cos(math.radians(angle)))
    y = int(300 - 200 * math.sin(math.radians(angle)))
    canvas.coords(point, x+7, y+7, x-7, y-7)
    angle += direction
    if angle <= -360:
        angle = 0
    root.after(speed, move_point)
    
direction = 1    
angle = 0
speed = int(input('Выберете скорость: '))
move_point()
root.mainloop()


# In[ ]:




