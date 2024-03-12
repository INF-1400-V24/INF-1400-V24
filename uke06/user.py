from media import Picture, Video
from random import randint

class User:

    def __init__(self, username):
        self.username = username
        self.media = []
        self.following = []

    def upload_media(self, filename, text):
        file_ext = filename[-3:]
        if file_ext not in ["png", "mp4"]:
            raise Exception("Can only upload videos or pictures")
        if file_ext == "png":
            self.media.append(Picture(filename, text, randint(40, 400)))
        else:
            self.media.append(Video(filename, text, randint(10, 100)))

    def show_profile(self):
        for media in self.media:
            media.show()

    def get_most_popular(self):
        if len(self.media) == 0:
            raise Exception("No media to fetch, can't get popular")
        most_likes = -1
        most_popular = None
        for media in self.media:
            if media.likes > most_likes:
                most_likes = media.likes
                most_popular = media
        return most_popular
    
    def follow(self, other_user):
        self.following.append(other_user)

    def show_feed(self):
        feed = []
        for user in self.following:
            feed.append(user.get_most_popular())
        for media in feed:
            media.show()

    def __add__(self, other):
        new_username = self.username
        new_media_list = self.media + other.media
        new_following_list = self.following + other.following
        new_user = User(new_username)
        new_user.media = new_media_list
        new_user.following = new_following_list
        return new_user
    
    def __getitem__(self, index):
        return self.media[index]
    
    def __setitem__(self, index, item):
        self.media[index] = item
    

if __name__ == "__main__":
    u1 = User("henrik.lovold")
    u1.upload_media("lol.png", "My brother looks weird lol #roflmao")
    u1.upload_media("skibidi.mp4", "Real skibidi rizz in Ohio #memes")

    u2 = User("brattkortmemes")
    u2.upload_media("funny.png", "Teit måte å klatre på as #joika")
    u2.upload_media("climber.mp4", "Sånn skal det gjøres #fåsds #crag")

    u3 = User("car_memes")
    u3.upload_media("car.png", "Look at my VW Polo #browncar")
    
    u4 = User("failarmy")
    u4.upload_media("haha.mp4", "Fails in Ohio #fail #lol #wtf")

    new_meme_user = u3 + u4

    new_meme_user[1] = Video("vid.mp4", "Boring video", 0)
    new_meme_user.show_profile()

"""
    u1.follow(u2)
    u1.follow(u3)
    u1.follow(u4)

    u1.show_feed()
"""