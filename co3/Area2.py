from graphics.RectFunctions import RectArea
from graphics.circfunctions import CirPerimeter
from graphics.DGraphics.spherefunctions import SpArea
from graphics.DGraphics.CuboidFunctions import CubPerimeter

#Rectangle
l=int(input("enter length: "))
b=int(input("enter braedth: "))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle Perimeter=",RectPerimeter(l,b))

#Circle
r=int(input("enter radius of Circle: "))
print("Circle Area =",CirArea(r))
print("Circle Perimeter=",CirPerimeter(r))

#Sphere
r=int(input("enter radius of Sphere: "))
print("Sphere Area=",SpArea(r))
print("Sphere Volume=",SpPerimeter(r))


#Cuboid

l = int(input("Enter cuboid length: "))
b = int(input("Enter cuboid breadth: "))
h = int(input("Enter cuboid height: "))
print("Cuboid Area = ",CubArea(l,b,h))
print("{Cuboid Perimeter = ",CubPerimeter(l,b,h))
