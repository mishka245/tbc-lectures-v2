
class Square:
    def __init__(self, s = 1):
        self.side = s

    def area(self):
        return self.side * self.side


s1 = Square(10)  # Object initiation - object creation
s2 = Square(16)
s3 = Square()
print(type(s1), s1.area())
print(type(s2), s2.area())
print(type(s3), s3.area())







