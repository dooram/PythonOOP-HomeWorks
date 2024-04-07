import tkinter as tk
import turtle as t
from math import sqrt

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        self.perimeter = 2*(self.a+self.b)
        perimeter_label.config(text=f"Per = {self.perimeter}")

    def area(self):
        self.area = self.a*self.b
        area_label.config(text=f"Area = {self.area}")

    def drawing(self):
        t.clear()
        t.penup()
        t.hideturtle()
        t.setpos(-200, 200)
        t.pensize(3)
        t.showturtle()
        t.pendown()
        for i in range(2):
            t.forward(self.a*5)
            t.right(90)
            t.forward(self.b*5)
            t.right(90)

class Square:
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        self.perimeter = 4*self.a
        perimeter_label.config(text=f"Per = {self.perimeter}")

    def area(self):
        self.area = self.a**2
        area_label.config(text=f"Area = {self.area}")

    def drawing(self):
        t.clear()
        t.penup()
        t.hideturtle()
        t.setpos(-200, 200)
        t.pensize(3)
        t.showturtle()
        t.pendown()
        for i in range(4):
            t.forward(self.a*5)
            t.right(90)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        self.perimeter = self.a+self.b+self.c
        perimeter_label.config(text=f"Per = {self.perimeter}")

    def area(self):
        self.p = (self.a+self.b+self.c)/2
        self.area = round(sqrt(self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c)), 2)
        area_label.config(text=f"Area = {self.area}")

    def drawing(self):
        t.clear()
        t.penup()
        t.hideturtle()
        t.setpos(-200, 200)
        t.pensize(3)
        t.showturtle()
        t.pendown()
        for i in range(3):
            t.forward(self.a*10)
            t.right(120)

class Circle:
    def __init__(self, r):
        self.r = r

    def diameter(self):
        self.diameter = 2*self.r
        perimeter_label.config(text=f"Diam = {self.diameter}")

    def area(self):
        self.area = round(3.14*(self.r**2), 2)
        area_label.config(text=f"Area = {self.area}")

    def drawing(self):
        t.clear()
        t.penup()
        t.hideturtle()
        t.setpos(0, -200)
        t.pensize(3)
        t.showturtle()
        t.pendown()
        t.circle(self.r*5)

def rectangle_shape():
    def perimeter():
        Nazar = Rectangle(int(a_Entry.get()), int(b_Entry.get()))
        Nazar.perimeter()
    def area():
        Nazar = Rectangle(int(a_Entry.get()), int(b_Entry.get()))
        Nazar.area()
    def draw():
        Nazar = Rectangle(int(a_Entry.get()), int(b_Entry.get()))
        Nazar.drawing()

    shape_title.config(text="Rectangle")
    a_Label.config(text="First side:")
    b_Label.config(text="Second side:")
    a_Label.grid(row=1, column=0, padx=5, pady=5)
    b_Label.grid(row=2, column=0, padx=5, pady=5)
    a_Entry.grid(row=1, column=1, padx=5, pady=5)
    b_Entry.grid(row=2, column=1, padx=5, pady=5)
    main_frame.pack_forget()
    shape_frame.pack()

    perimeter_button.config(command=perimeter)
    area_button.config(command=area)
    draw_button.config(command=draw)

def square_shape():
    def perimeter():
        Nazar = Square(int(a_Entry.get()))
        Nazar.perimeter()
    def area():
        Nazar = Square(int(a_Entry.get()))
        Nazar.area()
    def draw():
        Nazar = Square(int(a_Entry.get()))
        Nazar.drawing()

    shape_title.config(text="Square")
    a_Label.config(text="Side:")
    a_Label.grid(row=1, column=0, padx=5, pady=5)
    a_Entry.grid(row=1, column=1, padx=5, pady=5)
    main_frame.pack_forget()
    shape_frame.pack()

    perimeter_button.config(command=perimeter)
    area_button.config(command=area)
    draw_button.config(command=draw)

def triangle_shape():
    def perimeter():
        Nazar = Triangle(int(a_Entry.get()), int(b_Entry.get()), int(c_Entry.get()))
        Nazar.perimeter()
    def area():
        Nazar = Triangle(int(a_Entry.get()), int(b_Entry.get()), int(c_Entry.get()))
        Nazar.area()
    def draw():
        Nazar = Triangle(int(a_Entry.get()), int(b_Entry.get()), int(c_Entry.get()))
        Nazar.drawing()

    shape_title.config(text="Rectangle")
    a_Label.config(text="First side:")
    b_Label.config(text="Second side:")
    c_Label.config(text="Third side:")
    a_Label.grid(row=1, column=0, padx=5, pady=5)
    b_Label.grid(row=2, column=0, padx=5, pady=5)
    c_Label.grid(row=3, column=0, padx=5, pady=5)
    a_Entry.grid(row=1, column=1, padx=5, pady=5)
    b_Entry.grid(row=2, column=1, padx=5, pady=5)
    c_Entry.grid(row=3, column=1, padx=5, pady=5)
    main_frame.pack_forget()
    shape_frame.pack()

    perimeter_button.config(command=perimeter)
    area_button.config(command=area)
    draw_button.config(command=draw)

def circle_shape():
    def diameter():
        Nazar = Circle(int(a_Entry.get()))
        Nazar.diameter()
    def area():
        Nazar = Circle(int(a_Entry.get()))
        Nazar.area()
    def draw():
        Nazar = Circle(int(a_Entry.get()))
        Nazar.drawing()

    shape_title.config(text="Circle")
    a_Label.config(text="Radius:")
    a_Label.grid(row=1, column=0, padx=5, pady=5)
    a_Entry.grid(row=1, column=1, padx=5, pady=5)
    main_frame.pack_forget()
    shape_frame.pack()

    perimeter_button.config(text="Diameter", command=diameter)
    area_button.config(command=area)
    draw_button.config(command=draw)

root = tk.Tk()
root.title("Shapes")
root.geometry("300x200")
root.resizable(False, False)

main_frame = tk.Frame(root)
title_label = tk.Label(main_frame, text="Choose shape", font=("Consolas", 12))
rectangle_button = tk.Button(main_frame, text="Rectangle", font=("Arial", 10), command=rectangle_shape)
square_button = tk.Button(main_frame, text="Square", font=("Arial", 10), command=square_shape)
triangle_button = tk.Button(main_frame, text="Triangle", font=("Arial", 10), command=triangle_shape)
circle_button = tk.Button(main_frame, text="Circle", font=("Arial", 10), command=circle_shape)

title_label.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
rectangle_button.grid(row=3, column=0, padx=5, pady=5)
square_button.grid(row=3, column=1, padx=5, pady=5)
triangle_button.grid(row=3, column=2, padx=5, pady=5)
circle_button.grid(row=3, column=3, padx=5, pady=5)

main_frame.pack()

shape_frame = tk.Frame(root)
shape_title = tk.Label(shape_frame, text="", font=("Consolas", 10))
a_Label = tk.Label(shape_frame, text="", font=("Consolas", 10))
b_Label = tk.Label(shape_frame, text="", font=("Consolas", 10))
c_Label = tk.Label(shape_frame, text="", font=("Consolas", 10))
a_Entry = tk.Entry(shape_frame, font=("Consolas", 10), width=10)
b_Entry = tk.Entry(shape_frame, font=("Consolas", 10), width=10)
c_Entry = tk.Entry(shape_frame, font=("Consolas", 10), width=10)
perimeter_button = tk.Button(shape_frame, text="Perimeter", font=("Arial", 10))
area_button = tk.Button(shape_frame, text="Area", font="Arial, 10")
draw_button = tk.Button(shape_frame, text="Draw", font=("Arial", 10))
perimeter_label = tk.Label(shape_frame, text="", font=("Consolas", 10))
area_label = tk.Label(shape_frame, text="", font=("Consolas", 10))

shape_title.grid(row=0, column=1, padx=5, pady=5)
perimeter_button.grid(row=4, column=0, padx=5, pady=5)
draw_button.grid(row=4, column=1, padx=5, pady=5)
area_button.grid(row=4, column=2, padx=5, pady=5)
perimeter_label.grid(row=5, column=0, padx=5, pady=5)
area_label.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()