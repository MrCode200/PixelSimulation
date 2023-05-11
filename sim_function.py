import pygame
import json
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
    if v.SIMULATION_LVL == 0:
        v.SLIMY_SPRITE_NUMBER = 0
    elif v.SIMULATION_LVL == 1:
        v.SLIMY_SPRITE_NUMBER = 1

    while i <= v.SLIMY_SPRITE_NUMBER:
        IMG = PATH.format(i)
        SLIMY_JUMPING_SPRITE.append(pygame.transform.scale(pygame.image.load(IMG), (25, 25)))
        i += 1
    return SLIMY_JUMPING_SPRITE


def generate_food(num_generations):
    for food_ID in range(num_generations):
        new_food = cl.food(random.randrange(10, v.WIN_WIDTH), random.randrange(0, v.WIN_HEIGHT))
        v.FOOD_GROUP.add(new_food)


def generate_slimy(
        num_generations,
        pos_x=None, pos_y=None,
        SPEED=None,
        VISION=None):
    for slimy_ID in range(num_generations):
        # Create a Mutation code
        MUTATION = random.randint(1, 20)

        # check if slimy is binary fission and append DNA
        if SPEED != None:
            # if Mutation is a specific number create mutation
            if MUTATION == 1:
                new_slimy = cl.slimy(pos_x, pos_y, random.randint(1, 3), VISION)
            elif MUTATION == 2:
                new_slimy = cl.slimy(pos_x, pos_y, SPEED, v.SLIMY_VISION_STANDART + random.randrange(0, 35, 5))
            else:
                new_slimy = cl.slimy(pos_x, pos_y, SPEED, VISION)

        # else slimy is a random generated Slimy
        else:
            new_slimy = cl.slimy(
                random.randint(10, v.WIN_WIDTH), random.randint(0, v.WIN_HEIGHT),
                random.randint(1, 3), v.SLIMY_VISION_STANDART + random.randrange(0, 35, 5))

        v.DATA_SPEED.append(new_slimy.speed)
        v.DATA_VISION.append(new_slimy.radius)

        v.SLIMY_GROUP.add(new_slimy)


def info_board(WIN):
    # Create Data for Info board
    NUM_SLIMY = len(pygame.sprite.Group.sprites(v.SLIMY_GROUP))
    if v.ENERGY_SLIMY != 0 and NUM_SLIMY != 0:
        ENERGY_PER_SLIMY = round(v.ENERGY_SLIMY / NUM_SLIMY, 2)
    else:
        ENERGY_PER_SLIMY = 0

    # Render TEXT
    INFO_CYCLE = v.FONT.render("CYCLE: " + str(v.CYCLE), True, (0, 0, 0))
    INFO_SLIMY = v.FONT.render("SLIMYS: " + str(NUM_SLIMY), True, (0, 0, 0))
    INFO_ENERGY_PER_SLIMY = v.FONT.render("ENERGY PER SLIMY: " + str(ENERGY_PER_SLIMY), True, (0, 0, 0))
    INFO_ENERGY_SLIMY = v.FONT.render("ENERGY ALL SLIMY: " + str(int(v.ENERGY_SLIMY)), True, (0, 0, 0))
    INFO_ENERGY_FOOD = v.FONT.render("ENERGY ALL FOOD: " + str(round(v.ENERGY_FOOD, 1)), True, (0, 0, 0))
    INFO_BINARY_FISSION = v.FONT.render("ENERGY CONSUMPTION ALL SLIMY: " + str(round(v.ENERGY_CONSUMPTION, 1)), True,
                                        v.IBF_COLOR)

    # Draw info in board
    WIN.blit(INFO_CYCLE, (0, 0))
    WIN.blit(INFO_SLIMY, (0, 15))
    WIN.blit(INFO_ENERGY_PER_SLIMY, (0, 30))
    WIN.blit(INFO_ENERGY_SLIMY, (0, 45))
    WIN.blit(INFO_ENERGY_FOOD, (0, 60))
    WIN.blit(INFO_BINARY_FISSION, (0, 75))


# Generate Cycle
def cycle():
    if v.CYCLE_IN_FPS <= 60:
        v.CYCLE_IN_FPS += 1
    else:
        v.CYCLE_IN_FPS = 0
        v.CYCLE += 1

        # generate_food(v.NUM_OF_FOOD_START - len(pygame.sprite.Group.sprites(v.FOOD_GROUP)))
        generate_food(10)

        # reset energy available so it doesn't stack up
        v.ENERGY_SLIMY = 0
        v.ENERGY_FOOD = 0
        v.ENERGY_CONSUMPTION = 0

        # Create info for INFO_BOARD per cycle
        for num_of_slimy in v.SLIMY_GROUP.sprites():
            v.ENERGY_SLIMY += num_of_slimy.energy
            v.ENERGY_CONSUMPTION += 500 - num_of_slimy.energy
        for num_of_food in v.FOOD_GROUP.sprites():
            v.ENERGY_FOOD += num_of_food.energy

        if v.ENERGY_CONSUMPTION > v.ENERGY_FOOD:
            v.IBF_COLOR = (255, 0, 0)
        else:
            v.IBF_COLOR = (0, 0, 0)


# draw the pygame WIN
def draw(WIN):
    # Draw collision cicle
    WIN.fill((205, 133, 63))
    for num_of_slimy in v.SLIMY_GROUP.sprites():
        num_of_slimy.animate()
        pygame.draw.circle(WIN, num_of_slimy.vision_color, num_of_slimy.rect.center, num_of_slimy.radius)

    cycle()
    if v.INFO_BOARD_ON == True:
        info_board(WIN)

    v.FOOD_GROUP.draw(WIN)
    v.SLIMY_GROUP.draw(WIN)
    v.FOOD_GROUP.update()
    v.SLIMY_GROUP.update()

    pygame.display.update()
