#super class
class Shape:
    def __init__(self):
        self.color = "red"
        # self.sides = 0


#sub class
class Rectangle(Shape):
    def __init__(self, width, height):
        #call super class constructor
        super().__init__()
        #define instance variables
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    

#create an instance of Rectangle class
r1 = Rectangle(10, 20)

print(r1.color)
print(r1.area())
print(r1.perimeter())
print(r1.width) # AttributeError: 'Rectangle' object has no attribute 'sides'