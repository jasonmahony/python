from math import pi

class Circle:
    def __init__(self, r=0):
        self.r = r

    def getArea(self):
        return pi*self.r**2

    def getPerimeter(self):
        return 2*pi*self.r



circy = Circle(11)
print(circy.getArea())

# Should return 380.132711084365

circy = Circle(4.44)
print(circy.getPerimeter())

# Should return 27.897342763877365