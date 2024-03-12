from abc import ABC, abstractmethod

class Media(ABC):

    def __init__(self, filename, text, likes):
        self.filename = filename
        self.text = text
        self.likes = likes

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Picture(Media):

    def __init__(self, filename, text, likes):
        if filename[-3:] != "png":
            raise Exception("Pictures must be in png format!")
        super().__init__(filename, text, likes)

    def show(self):
        print("############")
        print("############")
        print("###Picture##")
        print("Placeholder#")
        print("############")
        print("############")
        print(self.text)
        print(self.likes, "likes!")
        print()

    def __str__(self):
        s = "PICTURE\n"
        s += "Filename: " + self.filename
        return s

class Video(Media):

    def __init__(self, filename, text, likes):
        if filename[-3:] != "mp4":
            raise Exception("Videos must be in mp4 format!")
        super().__init__(filename, text, likes)

    def show(self):
        print("************")
        print("************")
        print("***Video****")
        print("Placeholder*")
        print("************")
        print("************")
        print("************")
        print("************")
        print(self.text)
        print(self.likes, "likes!")
        print()

    def __str__(self):
        s = "VIDEO\n"
        s += "Filename: " + self.filename
        return s


if __name__ == "__main__":
    p = Picture("a.png", "My nice picture", 1000000000000)
    p.show()

    v = Video("vid.mp4", "Skibidi video", 4532)
    v.show()