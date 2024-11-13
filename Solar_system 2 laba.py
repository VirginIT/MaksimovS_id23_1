#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import math
import numpy as np

root = tk.Tk()
root.title("Солнечная система")
root.geometry("1600x800")

canvas = tk.Canvas(root, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)

def draw_circle(x, y, radius, color):
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="black")

class Planet:
    def __init__(self, x, y, radius, color, distance, speed, satellites=[]):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.distance = distance
        self.speed = speed
        self.angle = 0
        self.satellites = satellites

    def draw(self):
        x = self.x + self.distance * math.cos(self.angle)
        y = self.y + self.distance * math.sin(self.angle)
        draw_circle(x, y, self.radius, self.color)
        for satellite in self.satellites:
            satellite.update_position(x, y)
            satellite.draw()

    def update_position(self):
        self.angle += self.speed

class Satellite:
    def __init__(self, radius, color, distance, angle, speed):
        self.radius = radius
        self.color = color
        self.distance = distance
        self.speed = speed
        self.angle = angle
        self.x = 0
        self.y = 0

    def update_position(self, parent_x, parent_y):
        self.angle += self.speed
        self.x = parent_x + self.distance * math.cos(self.angle)
        self.y = parent_y + self.distance * math.sin(self.angle)

    def draw(self):
        draw_circle(self.x, self.y, self.radius, self.color)

earth_r = 5

satellites_earth = [
    Satellite(2, "gray", 12, 0, 0.1)
]

satellites_mars = [
    Satellite(1, "gray", 9, 0, 0.1),
    Satellite(1, "gray", 11, 180, 0.08)
]

satellites_jupiter = [
    Satellite(3.4, "burlywood2", 71, 0, 0.07),
    Satellite(3, "cornsilk2", 65.5, 0, 0.06),
    Satellite(2.3, "darkolivegreen3", 70, 0, 0.055),
    Satellite(2, "darksalmon", 68, 180, 0.065),
    Satellite(1.8, "coral", 73, 0, 0.08),
    Satellite(1.6,"gray", 67, 180, 0.05),
    Satellite(1.3, "gray", 65, 0, 0.095),
    Satellite(1.2, "gray", 74, 180, 0.075),
    Satellite(1.1, "gray", 72, 0, 0.09),
    Satellite(1, "gray", 77, 180, 0.08)
]

satellites_saturn = [
    Satellite(4, "darkolivegreen4", 69, 0, 0.07),
    Satellite(3, "gray", 63.5, 0, 0.06),
    Satellite(2, "darkolivegreen3", 68, 0, 0.045),
    Satellite(1.75, "coral", 66, 180, 0.065),
    Satellite(1.65, "gray", 71, 0, 0.08),
    Satellite(1.5, "gray", 69, 180, 0.05),
    Satellite(1, "gray", 63, 0, 0.095)
]

satellites_uran = [
    Satellite(2, "cornsilk2", 39, 0, 0.07),
    Satellite(1.95, "cornsilk2", 33.5, 180, 0.06),
    Satellite(1.5, "gray", 38, 0, 0.05),
    Satellite(1.3, "blue", 36, 180, 0.065),
    Satellite(1.1, "gray", 41, 0, 0.08)
]

satellites_neptun = [
    Satellite(2.5, "mediumpurple1", 39, 0, 0.07),
    Satellite(1.2, "maroon", 33.5, 180, 0.06),
    Satellite(1.05, "gray", 34, 0, 0.05),
    Satellite(0.75, "gray", 36, 180, 0.065)
]

planets = [
    Planet(800, 400, earth_r*0.38, "gray", 58, 0.0478),
    Planet(800, 400, earth_r*0.95, "orange", 88, 0.035),
    Planet(800, 400, earth_r, "chartreuse3", 129.6, 0.0298, satellites_earth),
    Planet(800, 400, earth_r*0.53, "red", 208, 0.0241, satellites_mars),
    Planet(800, 400, earth_r*11.2, "chocolate3", 350, 0.013, satellites_jupiter),
    Planet(800, 400, earth_r*9.45, "darkgoldenrod2", 460, 0.0096, satellites_saturn),
    Planet(800, 400, earth_r*4, "cyan", 560, 0.0068, satellites_uran),
    Planet(800, 400, earth_r*3.88, "cyan4", 700, 0.0054, satellites_neptun)
]

asteroids = []
for _ in range(360):
    i = np.random.randint(0, 360)
    x = 800 + 200 * math.cos(math.radians(i))
    y = 800 + 200 * math.sin(math.radians(i))
    radius = np.random.randint(1, 6)
    color = "gray75"
    asteroid = Satellite(radius, color, np.random.randint(230, 255), i, 0.01)
    asteroids.append(asteroid)

def update_animation():
    canvas.delete("all")
    sun = draw_circle(800, 400, 50, "yellow")
    for planet in planets:
        planet.update_position()
        planet.draw()
    for asteroid in asteroids:
        asteroid.update_position(800, 400)
        asteroid.draw()
    root.after(20, update_animation)

update_animation()
root.mainloop()


# In[ ]:




