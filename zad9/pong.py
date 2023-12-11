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

# SCORING
font = pygame.font.Font(None, 50)
player_score_counter = 0
enemy_score_counter = 0
scored = False

# BALL
ball_speed = 7
ball_radius = 10
ball_pos = [WIDTH / 2, HEIGHT / 2 - ball_radius]
angle = random.choice([random.randrange(0, 60), random.randrange(120, 240), random.randrange(300, 360)])
ball_velocity = pygame.math.Vector2(ball_speed, 0).rotate(angle)
ball_pos_vector = pygame.math.Vector2(ball_pos)
ball_future_vector = ball_pos_vector + ball_velocity

# PADDLES
paddle_width = 20
paddle_length = 100
paddle_speed = ball_speed + 2

# enemy paddle
enemy_paddle_pos_y = HEIGHT / 2
enemy_paddle_pos_centre_y = enemy_paddle_pos_y + paddle_length / 2
enemy_paddle_direction = 1
enemy_paddle = pygame.Rect(WIDTH - 60, HEIGHT / 2, paddle_width, paddle_length)

# player paddle
player_paddle_pos_y = HEIGHT / 2
player_paddle = pygame.Rect(40, HEIGHT / 2, paddle_width, paddle_length)

# LINE
line_width = 2
line = pygame.Rect(WIDTH / 2, 0, line_width, HEIGHT)

# other
wrong_steps_left = 0


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
sprite_ball = Block(ball_radius - 3, ball_radius - 3)
sprite_ball.rect.center = (WIDTH / 2, HEIGHT / 2)
sprite_ball.add(sprite_group_ball)

sprite_player_paddle = Block(paddle_width, paddle_length)
sprite_player_paddle.rect.topleft = (40, HEIGHT / 2)
sprite_player_paddle.add(sprite_group_paddles)

sprite_enemy_paddle = Block(paddle_width, paddle_length)
sprite_enemy_paddle.rect.topleft = (WIDTH - 60, HEIGHT / 2)
sprite_enemy_paddle.add(sprite_group_paddles)

# MAIN GAME LOOP
while True:
    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # INPUT
    keys = pygame.key.get_pressed()

    # PLAYER PADDLE MOVEMENT
    if keys[pygame.K_UP] and player_paddle_pos_y > 0:
        player_paddle = player_paddle.move(0, -paddle_speed)
        player_paddle_pos_y -= paddle_speed
    if keys[pygame.K_DOWN] and player_paddle_pos_y < HEIGHT - 100:
        player_paddle = player_paddle.move(0, paddle_speed)
        player_paddle_pos_y += paddle_speed

    # BALL MOVEMENT
    # wall bouncing
    if ball_pos_vector.y + ball_velocity.y > HEIGHT - ball_radius:
        ball_pos_vector.x = ball_pos_vector.x + ball_velocity.x
        ball_pos_vector.y = HEIGHT - ball_radius
        ball_velocity.y = -ball_velocity.y
    if ball_pos_vector.y + ball_velocity.y < ball_radius:
        ball_pos_vector.x = ball_pos_vector.x + ball_velocity.x
        ball_pos_vector.y = ball_radius
        ball_velocity.y = -ball_velocity.y

    # score counting
    if ball_pos_vector.x <= 0:
        scored = True
        enemy_score_counter += 1
    if ball_pos_vector.x >= WIDTH:
        scored = True
        player_score_counter += 1

    # ENEMY PADDLE MOVEMENT
    # moving when ball moves towards paddle
    if ball_velocity.x > 0:
        # moving accordingly to ball position if:
        # 1) there is no wrong movement frames left
        # 2) ball is far enough
        # 3) and random chance for wrong movement occurrence did not happen
        if (wrong_steps_left == 0 and random.randint(0, 220) > 2) or ball_pos_vector.x < WIDTH * 0.85:
            if (ball_pos_vector.y < enemy_paddle_pos_centre_y and ball_future_vector.y < enemy_paddle_pos_centre_y -
                    paddle_speed and enemy_paddle_pos_y > 0):
                enemy_paddle = enemy_paddle.move(0, -paddle_speed)
                enemy_paddle_pos_y -= paddle_speed
                enemy_paddle_direction = -1
            elif (ball_pos_vector.y > enemy_paddle_pos_centre_y and ball_future_vector.y > enemy_paddle_pos_centre_y +
                  paddle_speed and enemy_paddle_pos_y < HEIGHT - paddle_length):
                enemy_paddle = enemy_paddle.move(0, paddle_speed)
                enemy_paddle_pos_y += paddle_speed
                enemy_paddle_direction = 1
        # if conditions for good movement were not met, paddle moves into one direction for the randomised
        # number of frames
        else:
            if wrong_steps_left == 0:
                wrong_steps_left = random.randint(25, 35)
            if (enemy_paddle_direction == 1 and enemy_paddle_pos_y < HEIGHT - paddle_length) or (
                    enemy_paddle_direction == -1 and enemy_paddle_pos_y > 0):
                enemy_paddle = enemy_paddle.move(0, paddle_speed * enemy_paddle_direction)
                enemy_paddle_pos_y += paddle_speed * enemy_paddle_direction
            wrong_steps_left -= 1

    # CHECKING FOR COLLISIONS
    if pygame.sprite.collide_rect(sprite_ball, sprite_player_paddle):
        ball_pos_vector.x = player_paddle.x + paddle_width + ball_radius
        ball_velocity.x = -ball_velocity.x
    elif pygame.sprite.collide_rect(sprite_ball, sprite_enemy_paddle):
        ball_pos_vector.x = enemy_paddle.x - ball_radius
        ball_velocity.x = -ball_velocity.x

    # RESETTING BOARD
    if scored:
        if enemy_score_counter == 11 or player_score_counter == 11:
            pygame.quit()
            sys.exit(0)
        scored = False
        player_paddle_pos_y = HEIGHT / 2
        enemy_paddle_pos_y = HEIGHT / 2
        ball_pos = [WIDTH / 2, HEIGHT / 2 - ball_radius]
        ball_pos_vector = pygame.math.Vector2(ball_pos)
        angle = random.choice([random.randrange(0, 60), random.randrange(120, 240), random.randrange(300, 360)])
        ball_velocity = pygame.math.Vector2(ball_speed, 0).rotate(angle)
        player_paddle.update(40, HEIGHT / 2, paddle_width, paddle_length)
        enemy_paddle.update(WIDTH - 60, HEIGHT / 2, paddle_width, paddle_length)

    # UPDATING POSITIONS AND SPRITES
    ball_pos_vector = ball_pos_vector + ball_velocity
    ball_future_vector = ball_pos_vector + ball_velocity
    enemy_paddle_pos_centre_y = enemy_paddle_pos_y + paddle_length / 2

    sprite_group_ball.update(ball_pos_vector.x, ball_pos_vector.y)
    sprite_player_paddle.update(40, player_paddle_pos_y)
    sprite_enemy_paddle.update(WIDTH - 60, enemy_paddle_pos_y)

    # DRAWING
    screen.fill(black)
    pygame.draw.rect(screen, white, player_paddle)
    pygame.draw.rect(screen, white, enemy_paddle)
    pygame.draw.circle(screen, white, ball_pos_vector, ball_radius)
    pygame.draw.rect(screen, white, line)
    sprite_group_ball.draw(screen)
    sprite_group_paddles.draw(screen)

    # SCORING DISPLAY
    text_surf = font.render(str(player_score_counter) + "          " + str(enemy_score_counter), True, white)
    text_rect = text_surf.get_rect(center=(WIDTH / 2, HEIGHT / 4))
    screen.blit(text_surf, text_rect)

    pygame.display.flip()
    clock.tick(FPS)
