# sprite1.py
import sys
import pygame

# COLORS
black = (0, 0, 0)
gray = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# INITIALIZE THE GAME
pygame.init()   # to zawsze na starcie
size = (width, height) = (500, 500)
screen = pygame.display.set_mode(size)   # display Surface
pygame.display.set_caption('Creating Sprite')

# CLOCK
FPS = 60   # frames per second setting
clock = pygame.time.Clock()

sprite_group = pygame.sprite.Group()

sprite_red = Block(red, 50, 100)
sprite_red.rect.topleft = (200, 300)
sprite_group.add(sprite_red)

sprite_blue = Block(blue, 100, 100)
sprite_blue.rect.topleft = (100, 100)
sprite_group.add(sprite_blue)

sprite_green = Block(green, 100, 50)
sprite_green.rect.topleft = (150, 100)
sprite_group.add(sprite_green)

# MAIN GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # QUIT Event, pygame.locals.QUIT
            pygame.quit()   # deactivates the Pygame library
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                print("test kolizji sprite_red i sprite_blue")
                print(pygame.sprite.collide_rect(sprite_red, sprite_blue))

                print("test kolizji sprite_blue i sprite_green")
                print(sprite_blue.rect.colliderect(sprite_green.rect))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in sprite_group:   # iteracja po grupie
                if sprite.rect.collidepoint(event.pos):
                    print("trafiony {}".format(event.pos))

    sprite_group.update()   # wywołuje update() dla sprites
    screen.fill(black)
    sprite_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
