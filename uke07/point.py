
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((self.x + other.x)**2 - (self.y + other.y)**2)**0.5
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)



def dist(v1, v2):
    return ((v1[0] + v2[0])**2 - (v1[1] + v2[1])**2)**0.5


#Alternativ 1
p1 = (0, 1)
p2 = (0, 0)
p3 = p1 + p2
print(p3)


#Alternativ 2
p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = p1 + p2
print(p3.x, p3.y)