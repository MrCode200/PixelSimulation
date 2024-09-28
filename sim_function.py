import pygame
import classes as cl
import variables as v
import random


# appending Slime jumping sprite to array
def create_jump_sprite_slime():
    # prepare for creating jump sprite and Create a rare or normal sprite image
    i = 1
    SLIMY_JUMPING_SPRITE = []
    SHINY_CHANCE = random.randint(1, 10)
    if SHINY_CHANCE == 1:
        PATH = "Assets/Slimy_Animation/Pedaret_{}.png"
    else:
        PATH = "Assets/Slimy_Animation/Slimy_jumping{}.png"

    # Get all sprite images for diffrent Simulation levels
    if v.SIMULATION_LVL == 1:
        v.SLIMY_SPRITE_NUMBER = 1

    while i <= v.SLIMY_SPRITE_NUMBER:
        IMG = PATH.format(i)
        SLIMY_JUMPING_SPRITE.append(pygame.transform.scale(pygame.image.load(IMG), (25, 25)))
        i += 1
    return SLIMY_JUMPING_SPRITE


# appending One Eyed Bat sprite to array
def create_bat_sprite(egg_sprite):
    i = 1
    BAT_SPRITE = []

    if egg_sprite == False:
        PATH = "Assets/OneEyedBat_Animation/one_eye_bat{}.png"
        BAT_SPRITE_NUMBER = 8
    else:
        PATH = "Assets/OneEyedBat_Animation/one_eye_bat_egg{}.png"
        BAT_SPRITE_NUMBER = 5

    # Get all sprite images for diffrent Simulation levels
    if v.SIMULATION_LVL == 1:
        BAT_SPRITE_NUMBER = 1

    while i <= BAT_SPRITE_NUMBER:
        IMG = PATH.format(i)
        BAT_SPRITE.append(pygame.transform.scale(pygame.image.load(IMG), (40, 40)))
        i += 1
    return BAT_SPRITE


def generate_food(num_generations):
    for food_ID in range(num_generations):
        new_food = cl.food(random.randrange(20, v.WIN_WIDTH-20), random.randrange(20, v.WIN_HEIGHT-20))
        v.FOOD_GROUP.add(new_food)


def generate_slimy(
        num_generations,
        pos_x=None, pos_y=None,
        SPEED=None,
        VISION=None):
    for slimy_ID in range(num_generations):

        # else slimy is a random generated Slimy
        if SPEED is None:
            new_slimy = cl.slimy(
                random.randint(10, v.WIN_WIDTH), random.randint(0, v.WIN_HEIGHT),
                round(random.uniform(1, 3), 3), v.SLIMY_VISION_STANDART + round(random.uniform(0, 35), 3))
        else:
            new_slimy = cl.slimy(pos_x + random.randrange(-20, 20), pos_y + random.randrange(-20, 20),
                                 SPEED + round(random.uniform(-0.2, 0.2), 3), VISION + round(random.uniform(-1, 1), 3))

        v.DATA_SPEED_SLIMY.append(new_slimy.speed)
        v.DATA_VISION_SLIMY.append(new_slimy.radius)
        v.DATA_CYCLE_SLIMY.append(v.CYCLE)

        v.SLIMY_GROUP.add(new_slimy)
        v.TOTAL_SLIMY += 1


def generate_bat(num_generations, pos_x=None, pos_y=None, SPEED=None, VISION=None):
    for BAT_ID in range(num_generations):
        if pos_x is None:
            new_bat = cl.bat(random.randint(10, v.WIN_WIDTH), random.randint(0, v.WIN_HEIGHT),
                             round(random.uniform(1, 4), 3), v.BAT_VISION_STANDART + round(random.uniform(0, 35), 3))
        else:
            new_bat = cl.bat(pos_x, pos_y,
                             SPEED + round(random.uniform(-0.2, 0.2), 3), VISION + round(random.uniform(-1, 1), 3))

        v.DATA_SPEED_BAT.append(new_bat.speed)
        v.DATA_VISION_BAT.append(new_bat.radius)
        v.DATA_CYCLE_BAT.append(v.CYCLE)

        v.BAT_GROUP.add(new_bat)


def info_board(WIN):
    # Create Data for Info board
    NUM_SLIMY = len(pygame.sprite.Group.sprites(v.SLIMY_GROUP))
    NUM_BAT = len(pygame.sprite.Group.sprites(v.BAT_GROUP))
    if NUM_SLIMY != 0:
        ENERGY_PER_SLIMY = round(v.ENERGY_SLIMY / NUM_SLIMY, 2)
    else:
        ENERGY_PER_SLIMY = 0
    if NUM_BAT != 0:
        ENERGY_PER_BAT = round(v.BAT_ENERGY / NUM_BAT, 2)
    else:
        ENERGY_PER_BAT = 0

    # Render TEXT
    INFO_CYCLE = v.FONT.render("CYCLE: " + str(v.CYCLE), True, (0, 0, 0))
    INFO_SLIMY = v.FONT.render("SLIMYS: " + str(NUM_SLIMY), True, (0, 0, 0))
    INFO_TOTAL_SLIMY = v.FONT.render("TOTAL SLIMYS: " + str(v.TOTAL_SLIMY), True, (0, 0, 0))
    INFO_ENERGY_PER_SLIMY = v.FONT.render("ENERGY PER SLIMY: " + str(ENERGY_PER_SLIMY), True, (0, 0, 0))
    INFO_ENERGY_PER_BAT = v.FONT.render("ENERGY PER BAT: " + str(ENERGY_PER_BAT), True, (0, 0, 0))
    INFO_ENERGY_SLIMY = v.FONT.render("ENERGY ALL SLIMY: " + str(int(v.ENERGY_SLIMY)), True, (0, 0, 0))
    INFO_ENERGY_FOOD = v.FONT.render("ENERGY ALL FOOD: " + str(round(v.ENERGY_FOOD, 1)), True, (0, 0, 0))
    INFO_BINARY_FISSION = v.FONT.render("ENERGY REPRODUCTION ALL SLIMY: " + str(round(v.ENERGY_REPRODUCTION, 1)), True,
                                        v.IBF_COLOR)

    # Draw info in board
    WIN.blit(INFO_CYCLE, (0, 0))
    WIN.blit(INFO_SLIMY, (0, 15))
    WIN.blit(INFO_TOTAL_SLIMY, (0, 30))
    WIN.blit(INFO_ENERGY_PER_SLIMY, (0, 45))
    WIN.blit(INFO_ENERGY_PER_BAT, (0, 60))
    WIN.blit(INFO_ENERGY_SLIMY, (0, 75))
    WIN.blit(INFO_ENERGY_FOOD, (0, 90))
    WIN.blit(INFO_BINARY_FISSION, (0, 105))


# Generate Cycle
def cycle():
    if v.CYCLE_IN_FPS <= 60:
        v.CYCLE_IN_FPS += 1
    else:
        v.CYCLE_IN_FPS = 0
        v.CYCLE += 1

        generate_food(20)

        # reset energy available so it doesn't stack up
        v.ENERGY_SLIMY = 0
        v.ENERGY_FOOD = 0
        v.ENERGY_REPRODUCTION = 0
        v.BAT_ENERGY = 0

        if v.INFO_BOARD_ON == True:
            # Create info for INFO_BOARD per cycle
            for num_of_bat in v.BAT_GROUP.sprites():
                v.BAT_ENERGY += num_of_bat.energy
            for num_of_slimy in v.SLIMY_GROUP.sprites():
                v.ENERGY_SLIMY += num_of_slimy.energy
                v.ENERGY_REPRODUCTION += 500 - num_of_slimy.energy
            for num_of_food in v.FOOD_GROUP.sprites():
                v.ENERGY_FOOD += num_of_food.energy

            if v.ENERGY_REPRODUCTION > v.ENERGY_FOOD:
                v.IBF_COLOR = (200, 0, 0)
            else:
                v.IBF_COLOR = (0, 0, 0)


# draw the pygame WIN
def draw(WIN):
    # Draw collision cicle
    WIN.fill((205, 133, 63))
    if v.SIMULATION_LVL == 2:
        for num_of_slimy in v.SLIMY_GROUP.sprites():
            pygame.draw.circle(WIN, num_of_slimy.vision_color, num_of_slimy.rect.center, num_of_slimy.radius)
        for num_of_bat in v.BAT_GROUP.sprites():
            pygame.draw.circle(WIN, (0, 200, 0), num_of_bat.rect.center, num_of_bat.radius)
            

    cycle()
    if v.INFO_BOARD_ON == True:
        info_board(WIN)

    v.FOOD_GROUP.draw(WIN)
    v.SLIMY_GROUP.draw(WIN)
    v.BAT_GROUP.draw(WIN)
    v.FOOD_GROUP.update()
    v.SLIMY_GROUP.update()
    v.BAT_GROUP.update()

    pygame.display.update()
