from quest2 import *


'''
To create and draw a rectangle, an object of the rectangle class is created.
Parameters are two points, two conrers of the rectangle [eg: the bottomLeft and topRight corner]
The area and perimeter of the rectangles can be printed using getArea() and getPerimeter()
Also, using the overlap function with two rectangles as parameters, True or False is returned, depending on whether they intersect or not
Different scenarios are implemented here
'''

rOne = rectangle(g.Point(10,10),g.Point(40,40))
print("Area of rOne: ", rOne.getArea())
print("Perimeter of rOne: ", rOne.getPerimeter())

rTwo = rectangle(g.Point(15,15),g.Point(50,25))
print("Area of rTwo: ", rTwo.getArea())
print("Perimeter of rTwo: ", rTwo.getPerimeter())

print(overlap(rOne, rTwo))  #rOne and rTwo intersect. Thus, the function returns True

print("--------------------------------------------------------")


rThree = rectangle(g.Point(100,10),g.Point(200,40))
print("Area of rThree: ", rThree.getArea())
print("Perimeter of rThree: ", rThree.getPerimeter())

rFour = rectangle(g.Point(250,10),g.Point(350,40))
print("Area of rFour: ", rFour.getArea())
print("Perimeter of rFour: ", rFour.getPerimeter())

print(overlap(rThree, rFour))
'''rThree and rFour do not intersect. They are the second set of rectangles.
rThree is beside rFour. Thus, the function returns False'''

print("--------------------------------------------------------")

rFive = rectangle(g.Point(400,10),g.Point(500,40))
print("Area of rFive: ", rFive.getArea())
print("Perimeter of rFive: ", rFive.getPerimeter())

rSix = rectangle(g.Point(400,50),g.Point(500,80))
print("Area of rSix: ", rSix.getArea())
print("Perimeter of rSix: ", rSix.getPerimeter())

print(overlap(rFive, rSix))
'''rFive and rSix do not intersect. They are the third set of rectangles.
rFive is above rSix. Thus, the function returns False'''


