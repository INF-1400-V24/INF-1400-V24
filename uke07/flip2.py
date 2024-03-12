
class Vec2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    

def vec_flip1(v):
    x = v.x
    y = v.y
    v.x = y
    v.y = x

def vec_flip2(v):
    v = Vec2(v.y, v.x)
    return v
    
if __name__ == "__main__":
    v1 = Vec2(1, 2)
    print(v1)
    v1 = vec_flip2(v1)
    print(v1)
