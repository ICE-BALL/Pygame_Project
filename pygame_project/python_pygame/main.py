import os
import pygame

pygame.init()

screen_width = 1500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("magic war")

os_path = os.path.dirname(__file__)
image_path = os.path.join(os_path, "images")
skill_path = os.path.join(os_path, "skill")
sound_path = os.path.join(os_path, "sound")

# font
game_font = pygame.font.Font(None, 40)

clock = pygame.time.Clock()

# sound
main_song = pygame.mixer.Sound(os.path.join(sound_path, "main.mp3"))
main_song.play(-1)
over_sound = pygame.mixer.Sound(os.path.join(sound_path, "game_over_sound.mp3"))
ok_button = pygame.mixer.Sound(os.path.join(sound_path, "ok_button.mp3"))
freeze_sound = pygame.mixer.Sound(os.path.join(sound_path, "wind.mp3"))

# game over background
over_background = pygame.image.load(os.path.join(image_path, "game_over.png"))
over_background_size = over_background.get_rect().size
over_background_width = over_background_size[0]
over_background_height = over_background_size[1]
over_background_x_pos = 1500
over_background_y_pos = 0
game_over = False

# background
background = pygame.image.load(os.path.join(image_path, "magic_background.png"))
background_size = background.get_rect().size
background_width = background_size[0]
background_height = background_size[1]
background_x_pos = 0
background_y_pos = 0

# senter line
senter_line = pygame.image.load(os.path.join(image_path, "center_line.png"))
senter_line_size = senter_line.get_rect().size
senter_line_width = senter_line_size[0]
senter_line_height = senter_line_size[1]
senter_line_x_pos = 0
senter_line_y_pos = (screen_height / 2) - (senter_line_height / 2)


# heal spot
heal_spot = pygame.image.load(os.path.join(image_path, "background_sircle.png"))
heal_spot_size = heal_spot.get_rect().size
heal_spot_width = heal_spot_size[0]
heal_spot_height = heal_spot_size[1]
heal_spot_x_pos = (screen_width / 2) - (heal_spot_width / 2)
heal_spot_y_pos = (screen_height / 2 - senter_line_height / 2) - 200 + 10

# heal spot2
heal2_spot = pygame.image.load(os.path.join(image_path, "background_sircle.png"))
heal2_spot_size = heal2_spot.get_rect().size
heal2_spot_width = heal2_spot_size[0]
heal2_spot_height = heal2_spot_size[1]
heal2_spot_x_pos = (screen_width / 2) - (heal_spot_width / 2)
heal2_spot_y_pos = (screen_height / 2 + senter_line_height / 2) - 10

# tower
tower = pygame.image.load(os.path.join(image_path, "magic_tower.png"))
tower_size = tower.get_rect().size
tower_width = tower_size[0]
tower_height = tower_size[1]
tower_x_pos = 190
tower_y_pos = (screen_height / 2 - senter_line_height / 2) - tower_height + 10

# enemy tower
enemy_tower = pygame.image.load(os.path.join(image_path, "magic_tower.png"))
enemy_tower_size = enemy_tower.get_rect().size
enemy_tower_width = enemy_tower_size[0]
enemy_tower_height = enemy_tower_size[1]
enemy_tower_x_pos = 1200
enemy_tower_y_pos = (screen_height / 2 - senter_line_height / 2) - tower_height + 10

# gate
gate = pygame.image.load(os.path.join(image_path, "gate.png"))
gate_size = gate.get_rect().size
gate_width = gate_size[0]
gate_height = gate_size[1]
gate_x_pos = 0
gate_y_pos = screen_height / 2 - gate_height

# enemy_gate
enemy_gate = pygame.image.load(os.path.join(image_path, "gate.png"))
enemy_gate_size = enemy_gate.get_rect().size
enemy_gate_width = enemy_gate_size[0]
enemy_gate_height = enemy_gate_size[1]
enemy_gate_x_pos = screen_width - enemy_gate_width
enemy_gate_y_pos = gate_y_pos

# heal
heal_totem = pygame.image.load(os.path.join(image_path, "heal_totem.png"))
heal_totem_size = heal_totem.get_rect().size
heal_totem_width = heal_totem_size[0]
heal_totem_height = heal_totem_size[1]
heal_totem_x_pos = (screen_width / 2) - (heal_totem_width / 2)
heal_totem_y_pos = heal_spot_y_pos + 40

# another heal
heal2_totem = pygame.image.load(os.path.join(image_path, "heal_totem.png"))
heal2_totem_size = heal2_totem.get_rect().size
heal2_totem_width = heal2_totem_size[0]
heal2_totem_height = heal2_totem_size[1]
heal2_totem_x_pos = (screen_width / 2) - (heal2_totem_width / 2)
heal2_totem_y_pos = heal2_spot_y_pos + 40

# skill speed up
speed_up = []
speed_up.append(pygame.image.load(os.path.join(skill_path, "speed_up_use.png")))
speed_up.append(pygame.image.load(os.path.join(skill_path, "speed_up_time.png")))
speed_up_image_num = 0
speed_up_size = speed_up[speed_up_image_num].get_rect().size
speed_up_width = speed_up_size[0]
speed_up_height = speed_up_size[1]
speed_up_x_pos = 1300
speed_up_y_pos = 600
speed_up_use = False
speed_up_sleep = False

# skill freeze
freeze = []
freeze.append(pygame.image.load(os.path.join(skill_path, "freeze.png")))
freeze.append(pygame.image.load(os.path.join(skill_path, "freeze_time.png")))
freeze_image_num = 0
freeze_size = freeze[freeze_image_num].get_rect().size
freeze_width = freeze_size[0]
freeze_height = freeze_size[1]
freeze_x_pos = (screen_width - speed_up_width) - freeze_width
freeze_y_pos = 600
freeze_use = False
freeze_sleep = False

# main sprite
wizard = pygame.image.load(os.path.join(image_path, "Wizard.png"))
wizard_size = wizard.get_rect().size
wizard_width = wizard_size[0]
wizard_height = wizard_size[1]
wizard_x_pos = 0
wizard_y_pos = (screen_height / 2 - senter_line_height / 2) - wizard_height

# bot
bot = pygame.image.load(os.path.join(image_path, "mob.png"))
bot_size = bot.get_rect().size
bot_width = bot_size[0]
bot_height = bot_size[1]
bot_x_pos = gate_x_pos + bot_width
bot_y_pos = screen_height / 2 - bot_height

# enemy bot
enemy_bot = []
enemy_bot.append(pygame.image.load(os.path.join(image_path, "enemy_mob.png")))
enemy_bot.append(pygame.image.load(os.path.join(image_path, "enemy_mob_freeze.png")))
enemy_bot_image_num = 0
enemy_bot_size = enemy_bot[enemy_bot_image_num].get_rect().size
enemy_bot_width = enemy_bot_size[0]
enemy_bot_height = enemy_bot_size[1]
enemy_bot_x_pos = screen_width - enemy_bot_width - enemy_gate_width
enemy_bot_y_pos = screen_height / 2 - enemy_bot_height

# fire ball
fire_ball_image_num = 0
fire_ball = []
fire_ball.append(pygame.image.load(os.path.join(image_path, "fire_ball.png")))
fire_ball.append(pygame.image.load(os.path.join(image_path, "fire_ball_pop.png")))
fire_ball_size = fire_ball[fire_ball_image_num].get_rect().size
fire_ball_width = fire_ball_size[0]
fire_ball_height = fire_ball_size[1]
fire_ball_x_pos = tower_x_pos
fire_ball_y_pos = tower_y_pos

# bot HP
bot_hp = 50
enemy_bot_hp = 50

# bot hp
bot_hp_text = game_font.render("HP : {0}".format(bot_hp),True,(255, 255, 255))
bot_hp_text_size = bot_hp_text.get_rect().size
bot_hp_text_width = bot_hp_text_size[0]
bot_hp_text_height = bot_hp_text_size[1]
bot_hp_text_x_pos = (bot_x_pos / 2 + bot_hp_text_width / 2) + 20
bot_hp_text_y_pos = bot_y_pos - 50

# enemy_bot hp
bot_hp_enemy = game_font.render("HP : {0}".format(bot_hp),True,(255, 255, 255))
bot_hp_enemy_size = bot_hp_enemy.get_rect().size
bot_hp_enemy_width = bot_hp_enemy_size[0]
bot_hp_enemy_height = bot_hp_enemy_size[1]
bot_hp_enemy_x_pos = (enemy_bot_x_pos - bot_hp_enemy_width) + 100
bot_hp_enemy_y_pos = enemy_bot_y_pos - 50

# bot speed
bot_speed = 0.5
enemy_bot_speed = 0.5

# score
score = 0

# enemy score
enemy_score = 0

# game time
game_time = 210
game_ticks = pygame.time.get_ticks()

pop = False

running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and speed_up_sleep == False:
                ok_button.play()
                speed_up_use = True
                speed_up_sleep = True
            if event.key == pygame.K_w and freeze_sleep == False:
                ok_button.play()
                freeze_sound.play()
                freeze_use = True
                freeze_sleep = True
            if event.key == pygame.K_SPACE and game_over == True:
                ok_button.play()
                over_sound.stop()
                main_song.play(-1)
                score = 0
                enemy_score = 0
                game_time = 5
                game_ticks = pygame.time.get_ticks()
                game_over = False

    # skill "e" speed up
    if speed_up_use == True:
        bot_speed = 1.5

        elapsed_time = (pygame.time.get_ticks() - speed_start_ticks) / 1000

        if speed_total_time - elapsed_time <= 0:
            speed_up_use = False

    if speed_up_use == False:
        # speed skill time maintain
        speed_total_time = 3
        speed_start_ticks = pygame.time.get_ticks()

        bot_speed = 0.5

    if speed_up_sleep == True:
        sleep_elapsed_time = (pygame.time.get_ticks() - delay_start_ticks) / 1000
        speed_up_image_num = 1

        if delay_total_time - sleep_elapsed_time <= 0:
            speed_up_sleep = False

    if speed_up_sleep == False:
        speed_up_image_num = 0

        # speed skill time delay
        delay_total_time = 7
        delay_start_ticks = pygame.time.get_ticks()

    # skill "w" freeze
    if freeze_use == True:
        enemy_bot_speed = 0
        enemy_bot_image_num = 1

        freeze_elapsed_time = (pygame.time.get_ticks() - freeze_start_ticks) / 1000

        if freeze_total_time - freeze_elapsed_time <= 0:
            freeze_use = False

    if freeze_use == False:
        # freeze skill time maintain
        freeze_total_time = 5
        freeze_start_ticks = pygame.time.get_ticks()

        enemy_bot_image_num = 0
        enemy_bot_speed = 0.5

    if freeze_sleep == True:
        freeze_sleep_elapsed_time = (pygame.time.get_ticks() - freeze_delay_start_ticks) / 1000
        freeze_image_num = 1

        if freeze_delay_total_time - freeze_sleep_elapsed_time <= 0:
            freeze_sleep = False

    if freeze_sleep == False:
        freeze_image_num = 0

        # freeze skill time delay
        freeze_delay_total_time = 12
        freeze_delay_start_ticks = pygame.time.get_ticks()

    bot_x_pos += bot_speed
    enemy_bot_x_pos -= enemy_bot_speed

    # rect
    bot_rect = bot.get_rect()
    bot_rect.left = bot_x_pos
    bot_rect.top = bot_y_pos

    enemy_gate_rect = enemy_gate.get_rect()
    enemy_gate_rect.left = enemy_gate_x_pos
    enemy_gate_rect.top = enemy_gate_y_pos

    gate_rect = gate.get_rect()
    gate_rect.top = gate_y_pos
    gate_rect.left = gate_x_pos

    enemy_bot_rect = enemy_bot[enemy_bot_image_num].get_rect()
    enemy_bot_rect.left = enemy_bot_x_pos
    enemy_bot_rect.top = enemy_bot_y_pos

    # fire ball rect
    fire_ball_rect = fire_ball[fire_ball_image_num].get_rect()
    fire_ball_rect.left = fire_ball_x_pos
    fire_ball_rect.top = fire_ball_y_pos

    if bot_rect.colliderect(enemy_bot_rect):
        enemy_bot_hp -= 0.1
        bot_hp -= 0.1

    if bot_rect.colliderect(enemy_gate_rect):
        if enemy_score >= 5:
            enemy_score -= 5
        else:
            enemy_score = 0
        score += 10
        bot_x_pos = gate_x_pos + bot_width

    if enemy_bot_rect.colliderect(gate_rect):
        if score >= 5:
            score -= 5
        else:
            score = 0
        enemy_score += 10
        enemy_bot_x_pos = screen_width - enemy_bot_width - enemy_gate_width

    enemy_score_memory = enemy_score
    score_memory = score

    # background
    screen.blit(background, (0, 0))

    # line
    screen.blit(senter_line, (senter_line_x_pos, senter_line_y_pos))

    # sircle
    screen.blit(heal_spot, (heal_spot_x_pos, heal_spot_y_pos))

    # sircle2
    screen.blit(heal2_spot, (heal2_spot_x_pos, heal2_spot_y_pos))
    
    # tower
    screen.blit(tower, (tower_x_pos, tower_y_pos))

    # enemy tower
    screen.blit(enemy_tower, (enemy_tower_x_pos, enemy_tower_y_pos))

    # gate
    screen.blit(gate, (gate_x_pos, gate_y_pos))

    # enemy gate
    screen.blit(enemy_gate, (enemy_gate_x_pos, enemy_gate_y_pos))

    # totem
    screen.blit(heal_totem, (heal_totem_x_pos, heal_totem_y_pos))

    # totem
    screen.blit(heal2_totem, (heal2_totem_x_pos, heal2_totem_y_pos))

    # sprite
    screen.blit(wizard, (wizard_x_pos, wizard_y_pos))

    # bot
    screen.blit(bot, (bot_x_pos, bot_y_pos))

    # fire ball
    screen.blit(fire_ball[fire_ball_image_num], (fire_ball_x_pos, fire_ball_y_pos))

    # enemy bot
    screen.blit(enemy_bot[enemy_bot_image_num], (enemy_bot_x_pos, enemy_bot_y_pos))

    # skill speed up
    screen.blit(speed_up[speed_up_image_num], (speed_up_x_pos, speed_up_y_pos))

    # key "e"
    keyE = game_font.render("E",True,(255, 255, 255))
    screen.blit(keyE,(speed_up_x_pos + 85, speed_up_y_pos - 20))

    # skill freeze
    screen.blit(freeze[freeze_image_num], (freeze_x_pos, freeze_y_pos))

    # key "w"
    keyW = game_font.render("w",True,(255, 255, 255))
    screen.blit(keyW,(freeze_x_pos + 85, freeze_y_pos - 20))

    # score
    score_text = game_font.render("score : {0}".format(score),True,(255, 255, 255))
    screen.blit(score_text, (screen_width / 2, 0))

    # 경과 시간 계산
    game_elapsed_time = (pygame.time.get_ticks() - game_ticks) / 1000

    # 타이머
    timer = game_font.render("time left: " + str(int(game_time - game_elapsed_time)), True, (255,255,255))

    #경과 시간 표시
    screen.blit(timer, (10, 10))

    # bot HP
    bot_hp_text_speed = bot_speed
    bot_hp_text_x_pos += bot_hp_text_speed
    screen.blit(bot_hp_text, (bot_hp_text_x_pos, bot_hp_text_y_pos))

    bot_hp_enemy_speed = enemy_bot_speed
    bot_hp_enemy_x_pos -= bot_hp_enemy_speed
    bot_hp_enemy = game_font.render("HP : {0}".format(bot_hp),True,(255, 255, 255))
    screen.blit(bot_hp_enemy, (bot_hp_enemy_x_pos, bot_hp_enemy_y_pos))

    if game_time - game_elapsed_time <= 0:
        game_over = True

    if game_over == True:
        main_song.stop()
        ok_button.stop()
        freeze_sound.stop()
        over_sound.play(-1)
        if score_memory > enemy_score_memory:
            result = "WIN!"
        elif score_memory < enemy_score_memory:
            result = "LOSE.."
        elif score_memory == enemy_score_memory:
            result = "tie"
        
        if score_memory > enemy_score_memory:
            result_enemy = "LOSE.."
        elif score_memory < enemy_score_memory:
            result_enemy = "WIN!"
        elif score_memory == enemy_score_memory:
            result_enemy = "tie"

        over_background_x_pos = 0
        bot_x_pos = gate_x_pos + bot_width
        enemy_bot_x_pos = screen_width - enemy_bot_width - enemy_gate_width
        freeze_use = False
        freeze_sleep = False
        speed_up_use = False
        speed_up_sleep = False

    elif game_over == False:
        over_background_x_pos = 1500

    # game over
    screen.blit(over_background, (over_background_x_pos, over_background_y_pos))

    if game_over == True:
        # result score
        result_score = game_font.render("score : {0}".format(score_memory),True,(255, 255, 255))
        screen.blit(result_score, (screen_width / 4, 400))

        result_score_enemy = game_font.render("enemy score : {0}".format(enemy_score_memory),True,(255, 255, 255))
        screen.blit(result_score_enemy, (screen_width / 1.5, 400))

        result = game_font.render("{0}".format(result),True,(255, 255, 255))
        result_size = result.get_rect().size
        result_width = result_size[0]

        enemy_result = game_font.render("{0}".format(result_enemy),True,(255, 255, 255))
        enemy_result_size = enemy_result.get_rect().size
        enemy_result_width = enemy_result_size[0]

        # restart
        restart = game_font.render("--press space to restart--",True,(255, 255, 255))
        restart_size = restart.get_rect().size
        restart_width = restart_size[0]
        screen.blit(restart, ((screen_width / 2) - (restart_width / 2), 550))

        screen.blit(result, (screen_width / 4, 450))
        screen.blit(enemy_result, (screen_width / 1.5, 450))
    
    pygame.display.update()

pygame.quit()