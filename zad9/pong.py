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
sprite_group_paddles = pygame.sprite.Group()
sprite_group_ball = pygame.sprite.Group()

# SPRITES AND ADDING TO GROUPS
paddle_width = 20
paddle_length = 100

sprite_ball = Block(7, 7)
sprite_ball.rect.center = (WIDTH / 2, HEIGHT / 2)
sprite_ball.add(sprite_group_ball)

sprite_left_paddle = Block(paddle_width, paddle_length)
sprite_left_paddle.rect.topleft = (40, HEIGHT / 2)
sprite_left_paddle.add(sprite_group_paddles)

sprite_right_paddle = Block(paddle_width, paddle_length)
sprite_right_paddle.rect.topleft = (WIDTH - 60, HEIGHT / 2)
sprite_right_paddle.add(sprite_group_paddles)

# MAKE SHAPES
# ball
ball_speed = 5
ball_pos = [WIDTH / 2, HEIGHT / 2 - 10]
ball_velocity = pygame.math.Vector2(ball_speed, 0).rotate(random.randrange(360))
ball_pos_vector = pygame.math.Vector2(ball_pos)
# paddles
enemy_paddle_counter = 0
player_paddle_pos_y = HEIGHT / 2
enemy_paddle_pos_y = HEIGHT / 2
left_paddle = pygame.Rect(40, HEIGHT / 2, paddle_width, paddle_length)
right_paddle = pygame.Rect(WIDTH - 60, HEIGHT / 2, paddle_width, paddle_length)

# MAIN GAME LOOP
while True:
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # INPUT
    keys = pygame.key.get_pressed()

    # player paddle
    if keys[pygame.K_UP] and player_paddle_pos_y > 0:
        left_paddle = left_paddle.move(0, -(ball_speed + 2))
        player_paddle_pos_y -= ball_speed + 2
    if keys[pygame.K_DOWN] and player_paddle_pos_y < HEIGHT - 100:
        left_paddle = left_paddle.move(0, ball_speed + 2)
        player_paddle_pos_y += ball_speed + 2

    # ball movement
    if ball_pos_vector.y + ball_velocity.y > HEIGHT - 10:
        ball_pos_vector.x = ball_pos_vector.x + ball_velocity.x
        ball_pos_vector.y = HEIGHT - 10
        ball_velocity.y = -ball_velocity.y
    if ball_pos_vector.y + ball_velocity.y < 10:
        ball_pos_vector.x = ball_pos_vector.x + ball_velocity.x
        ball_pos_vector.y = 10
        ball_velocity.y = -ball_velocity.y

    # enemy paddle
    if ball_velocity.x > 0 and enemy_paddle_counter != 3:
        if ball_pos_vector.y < enemy_paddle_pos_y + paddle_length/2 and ball_pos_vector.y + ball_velocity.y < enemy_paddle_pos_y - ball_speed - 2 + paddle_length/2 and enemy_paddle_pos_y > 0:
            right_paddle = right_paddle.move(0, -(ball_speed + 2))
            enemy_paddle_pos_y -= ball_speed + 2
            enemy_paddle_counter += 1
            print("Ball above", ball_pos_vector.y, enemy_paddle_pos_y + paddle_length/2)
        elif ball_pos_vector.y > enemy_paddle_pos_y + paddle_length/2 and ball_pos_vector.y + ball_velocity.y > enemy_paddle_pos_y + ball_speed + 2 + paddle_length/2 and enemy_paddle_pos_y < HEIGHT - paddle_length:
            right_paddle = right_paddle.move(0,  ball_speed + 2)
            enemy_paddle_pos_y += ball_speed + 2
            enemy_paddle_counter += 1
            print("Ball below", ball_pos_vector.y, enemy_paddle_pos_y + paddle_length/2)
    if enemy_paddle_counter == 3:
        enemy_paddle_counter = 0

    # checking for collisions
    if pygame.sprite.spritecollideany(sprite_ball, sprite_group_paddles) is not None:
        ball_velocity.x = -ball_velocity.x

    ball_pos_vector = ball_pos_vector + ball_velocity

    # UPDATING
    sprite_group_ball.update(ball_pos_vector.x, ball_pos_vector.y)
    sprite_left_paddle.update(40, player_paddle_pos_y)
    sprite_right_paddle.update(WIDTH - 60, enemy_paddle_pos_y)

    # DRAWING
    screen.fill(black)
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.circle(screen, white, ball_pos_vector, 10)
    sprite_group_ball.draw(screen)
    sprite_group_paddles.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
