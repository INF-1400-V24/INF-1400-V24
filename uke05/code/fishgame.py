import pygame
import random

SCREEN_X = 1024
SCREEN_Y = 768
BG_FILENAME = "underwater.jpg"
FISH_FILENAME = "cod.png"
HOOK_FILENAME = "hook.png"

# Initialize
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
background = pygame.image.load(BG_FILENAME)
background = pygame.transform.scale(background, (SCREEN_X, SCREEN_Y))
background.convert()

fish_img = pygame.image.load(FISH_FILENAME).convert_alpha()
hook_img = pygame.image.load(HOOK_FILENAME).convert_alpha()
hook_img = pygame.transform.scale(hook_img, (hook_img.get_width() / 20, hook_img.get_height() / 20))

pygame.mouse.set_visible(False)

# Hook sprite class
class HookSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = hook_img
        self.rect = pygame.rect.Rect(0, 0, self.image.get_width(), self.image.get_height())
    
    def update(self):
        mouse = pygame.mouse.get_pos()
        new_x = mouse[0] - 0.5*self.image.get_width()
        new_y = mouse[1] - 0.5*self.image.get_height()
        self.rect.x = new_x
        self.rect.y = new_y

# Fish sprite class
class FishSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.flip(fish_img, True, False)
        self.x = random.randint(0, SCREEN_X - fish_img.get_width())
        self.y = random.randint(0, SCREEN_Y - fish_img.get_width())
        self.rect = pygame.rect.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.speed = random.uniform(0, 1)

    def update(self):
        self.x = self.x + self.speed
        self.rect.x = self.x
        if self.x < 0:
            self.speed = abs(self.speed)
            self.image = pygame.transform.flip(self.image, True, False)
        if self.x > SCREEN_X - self.image.get_width():
            self.speed = -abs(self.speed)
            self.image = pygame.transform.flip(self.image, True, False)


# Create hook sprite and group
hook_group = pygame.sprite.Group()
hook = HookSprite()
hook_group.add(hook)

# Create fish sprites and fish group
fish_group = pygame.sprite.Group()
for _ in range(5):
    fish_group.add(FishSprite())


while True:

    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        x = pygame.sprite.groupcollide(hook_group, fish_group, False, True)

    screen.blit(background, (0, 0))

    fish_group.update()
    fish_group.draw(screen)

    hook_group.update()
    hook_group.draw(screen)

    pygame.display.update()