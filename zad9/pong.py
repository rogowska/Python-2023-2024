# Oliwia Rogowska #
#    Zadanie 9    #
#     Python      #
#   09.12.2023    #
###################

# ATARI PONG IMPLEMENTATION #

import sys
import pygame
import random

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)

# INITIALIZE THE GAME
pygame.init()
size = WIDTH, HEIGHT = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Atari Pong')

# CLOCK
FPS = 60
clock = pygame.time.Clock()


# SPRITE BLOCK
class Block(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.rect = self.image.get_rect()

    def update(self, new_x, new_y):
        self.rect.update(new_x, new_y, self.rect.width, self.rect.height)


# SPRITE GROUPS
sprite_group_palettes = pygame.sprite.Group()
sprite_group_ball = pygame.sprite.Group()

# SPRITES AND ADDING TO GROUPS
sprite_ball = Block(7, 7)
sprite_ball.rect.center = (WIDTH / 2, HEIGHT / 2)
sprite_ball.add(sprite_group_ball)

sprite_left_palette = Block(20, 100)
sprite_left_palette.rect.topleft = (40, HEIGHT / 2)
sprite_left_palette.add(sprite_group_palettes)

sprite_right_palette = Block(20, 100)
sprite_right_palette.rect.topleft = (WIDTH - 60, HEIGHT / 2)
sprite_right_palette.add(sprite_group_palettes)


# MAKE SHAPES
# ball
ball_pos = [WIDTH / 2, HEIGHT / 2 - 10]
ball_velocity = pygame.math.Vector2(3, 0).rotate(random.randrange(360))
ball_pos_vector = pygame.math.Vector2(ball_pos)
# palettes
player_palette_pos_y = HEIGHT / 2
left_palette = pygame.Rect(40, HEIGHT / 2, 20, 100)
right_palette = pygame.Rect(WIDTH - 60, HEIGHT / 2, 20, 100)

# MAIN GAME LOOP
while True:
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


    # INPUT
    keys = pygame.key.get_pressed()
    # player palette
    if keys[pygame.K_UP] and player_palette_pos_y > 0:
        left_palette = left_palette.move(0, -4)
        player_palette_pos_y -= 4
    if keys[pygame.K_DOWN] and player_palette_pos_y < 620:
        left_palette = left_palette.move(0, 4)
        player_palette_pos_y += 4
    # ball movement
    if ball_pos_vector.y + ball_velocity.y > HEIGHT - 10:
        ball_pos_vector.x = ball_pos_vector.x + ball_velocity.x
        ball_pos_vector.y = HEIGHT - 10
        ball_velocity.y = -ball_velocity.y
    if ball_pos_vector.y + ball_velocity.y < 10:
        ball_pos_vector.x = ball_pos_vector.x + ball_velocity.x
        ball_pos_vector.y = 10
        ball_velocity.y = -ball_velocity.y
    ball_pos_vector = ball_pos_vector + ball_velocity

    if pygame.sprite.spritecollideany(sprite_ball, sprite_group_palettes) is not None:
        ball_velocity.x = -ball_velocity.x

    # UPDATING
    sprite_group_ball.update(ball_pos_vector.x, ball_pos_vector.y)
    sprite_left_palette.update(40, player_palette_pos_y)
    sprite_right_palette.update(WIDTH - 60, player_palette_pos_y)

    # DRAWING
    screen.fill(black)
    pygame.draw.rect(screen, white, left_palette)
    pygame.draw.rect(screen, white, right_palette)
    pygame.draw.circle(screen, white, ball_pos_vector, 10)
    sprite_group_ball.draw(screen)
    sprite_group_palettes.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
