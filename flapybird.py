import pygame as pg
from sys import exit
from random import choice
#from f.constants import *

DISPLAY_WIDTH = 280
DISPLAY_HEIGHT = 512
DISPLAY_AREA = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

white = (255, 255, 255)


def animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(50, bird_rect.centery))

    return new_bird, new_bird_rect


def rotate(img):
    new_bird = pg.transform.rotate(img, - bird_move * 3)

    return new_bird


def create_pipe():
    random_pipe = choice(pipe_hei)
    top_pipe = pipe.get_rect(midbottom=(DISPLAY_WIDTH + 26, random_pipe - 150))
    bottom_pipe = pipe.get_rect(midtop=(DISPLAY_WIDTH + 26, random_pipe))

    return top_pipe, bottom_pipe


def draw_pipe(pipes):
    for p in pipes:
        if p.bottom >= DISPLAY_HEIGHT:
            display.blit(pipe, p)
        else:
            flip_pipe = pg.transform.flip(pipe, False, True)
            display.blit(flip_pipe, p)


def move_pipe(pipes):
    for p in pipes:
        p.centerx -= 5

    return pipes


def spawn_pipe():
    if event.type == pipe_spawn:
        pipe_list.append(create_pipe())


def remove_pipe(pipes):
    global obstacle_number

    if len(pipes) != 0:
        if pipes[0][0] + 52 <= 0:
            pipes.pop(0)
            pipes.pop(0)
            obstacle_number -= 2
    
    return pipes[:]


def move_floor():
    display.blit(floor, (floor_pos_x, DISPLAY_HEIGHT - floor_rect.height // 2))
    display.blit(floor, (floor_pos_x + DISPLAY_WIDTH, DISPLAY_HEIGHT - floor_rect.height // 2))


def check_obstacle_passed():
    global obstacle_number
    pipes = pipe_list[:]

    if len(pipes) > obstacle_number:
        if pipes[obstacle_number][0] + 52 <= 26:
            obstacle_number += 2
            point_snd.play()
            return True

    return False


def check_collision(pipes):
    for p in pipes:
        if bird_rect.colliderect(p):
            collide_snd.play()
            return False

    if bird_rect.top <= 0 or bird_rect.bottom >= DISPLAY_HEIGHT - floor_rect.height // 2:
        collide_snd.play()
        return False

    return True


def score_display(game_state):
    if game_state == 'main_game':
        score_font = font.render(str(int(score)), True, white)
        score_font_rect = score_font.get_rect(center=(DISPLAY_WIDTH // 2, 50))
        display.blit(score_font, score_font_rect)
    elif game_state == 'game_over':
        score_font = font.render(f'Score: {int(score)}', True, white)
        score_font_rect = score_font.get_rect(center=(DISPLAY_WIDTH // 2, 50))
        display.blit(score_font, score_font_rect)

        hight_score_font = font.render(f'High Score: {int(high_score)}', True, white)
        hight_score_font_rect = hight_score_font.get_rect(center=(DISPLAY_WIDTH // 2, 412))
        display.blit(hight_score_font, hight_score_font_rect)


def increment_score(scr, increment):
    if check_obstacle_passed():
        return scr + increment

    return scr


def score_update(scr, high_scr):
    if scr > high_scr:
        high_scr = scr

    return high_scr


'DISPLAY'
display = pg.display.set_mode(DISPLAY_AREA)
pg.display.set_caption('FlappyBird')

'BACKGROUND'
bg = pg.image.load('assets/images/sprites/Background.png').convert()
floor = pg.image.load('assets/images/sprites/Floor.png').convert_alpha()
floor_rect = floor.get_rect()
floor_pos_x = 0
pipe = pg.image.load('assets/images/sprites/Pipe.png')
pipe_list = []
pipe_spawn = pg.USEREVENT
obstacle_number = 0

pg.time.set_timer(pipe_spawn, 2400)
pipe_hei = [200, 300, 400]
bg_game_over = pg.image.load('assets/images/sprites/Game_Over.png')
bg_game_over_rect = bg_game_over.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 - 25))

'BIRD'
bird_down = pg.image.load('assets/images/sprites/Bird_down.png').convert_alpha()
bird_mid = pg.image.load('assets/images/sprites/Bird_mid.png').convert_alpha()
bird_up = pg.image.load('assets/images/sprites/Bird_up.png').convert_alpha()
bird_frames = [bird_down, bird_mid, bird_up]
bird_index = 0
bird = bird_frames[bird_index]
bird_rect = bird.get_rect(center=(50, DISPLAY_HEIGHT // 2))
bird_flap = pg.USEREVENT + 1
pg.time.set_timer(bird_flap, 200)
bird_move = 0
gravity = 0.25

'SOUND EFFECTS'
pg.mixer.init(44100, 16, 2, 512)
flap_snd = pg.mixer.Sound('assets/sounds/sound_effects/Flap.ogg')
collide_snd = pg.mixer.Sound('assets/sounds/sound_effects/Hit.ogg')
point_snd = pg.mixer.Sound('assets/sounds/sound_effects/Point.ogg')

'FONT'
pg.font.init()
font = pg.font.Font('assets/font/04B_19.ttf', 20)

'SCORE'
high_score = 0
score = high_score

'FPS'
clock = pg.time.Clock()
fps = 100

'LOOP'
game = True
while True:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and game:
                bird_move = 0
                bird_move -= 8
                flap_snd.play()
            elif event.key == pg.K_SPACE and not game:
                game = True
                pipe_list.clear()
                bird_move = 0
                bird_rect.center = (50, DISPLAY_HEIGHT // 2)
                score = 0
                obstacle_number = 0

        if event.type == bird_flap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird, bird_rect = animation()

        if event.type == pipe_spawn:
            pipe_list.extend(create_pipe())

    display.blit(bg, (0, 0))

    if game:
        # BIRD
        bird_move += gravity
        bird_rect.centery += int(bird_move)
        bird_rotate = rotate(bird)

        display.blit(bird_rotate, bird_rect)
        game = check_collision(pipe_list)

        # PIPE
        draw_pipe(pipe_list)
        pipe_list = move_pipe(pipe_list)
        pipe_list = remove_pipe(pipe_list)

        # SCORE
        score_display('main_game')
        score = increment_score(score, 1)

    else:
        display.blit(bg_game_over, bg_game_over_rect)

        # PIPE
        pipe_list = move_pipe(pipe_list)
        pipe_list = remove_pipe(pipe_list)
        
        # SCORE
        high_score = score_update(score, high_score)
        score_display('game_over')

    # FLOOR
    move_floor()
    if floor_pos_x <= -DISPLAY_WIDTH:
        floor_pos_x = 0
    floor_pos_x -= 1

    pg.display.update()
