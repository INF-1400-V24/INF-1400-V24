import pygame
import random

# Filene underwater.jpg, RainbowBall.png og GlowFrame.png
# er ikke inkludert her av royalty-grunner. Last ned egne
# filer og endre filnavn.

SCREEN_X = 1024
SCREEN_Y = 768
DIMENSIONS = (SCREEN_X, SCREEN_Y)
BG_FILENAME = "underwater.jpg"
BALL_FILENAME = "RainbowBall.png"
SQUARE_FILENAME = "GlowFrame.png"

pygame.init()

screen = pygame.display.set_mode(DIMENSIONS)
background = pygame.image.load(BG_FILENAME)
background = pygame.transform.scale(background, DIMENSIONS)
background.convert()

ball_img = pygame.image.load(BALL_FILENAME)
square_img = pygame.image.load(SQUARE_FILENAME)
ball_img = pygame.transform.scale(ball_img, (50, 50))
square_img = pygame.transform.scale(square_img, (50, 50))

class Element(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = random.randint(0, SCREEN_X - self.width)
        self.y = random.randint(0, SCREEN_Y - self.height)
        self.rect = pygame.rect.Rect(self.x, self.y,
                                     self.width, self.height)
        
class Square(Element):

    def __init__(self):
        super().__init__(square_img)

class Ball(Element):

    def __init__(self):
        super().__init__(ball_img)

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.y -= 1
        elif key[pygame.K_DOWN]:
            self.rect.y += 1
        elif key[pygame.K_RIGHT]:
            self.rect.x += 1
        elif key[pygame.K_LEFT]:
            self.rect.x -= 1


ball_group = pygame.sprite.Group()
square_group = pygame.sprite.Group()

ball_group.add(Ball())
for _ in range(10):
    square_group.add(Square())

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.sprite.groupcollide(ball_group, square_group, False, True)
    screen.blit(background, (0, 0))
    square_group.update()
    ball_group.update()
    square_group.draw(screen)
    ball_group.draw(screen)


    pygame.display.update()