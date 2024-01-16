
class Square:

    def __init__(self):
        self.player = 0

    def change_num(self, player):
        if self.player != 0:
            return False
        if player not in [1, 2]:
            return False
        self.player = player
        return True
    
    def __str__(self):
        return str(self.player)
    

if __name__ == "__main__":
    s = Square()
    s.change_num(10)
    print(s)
