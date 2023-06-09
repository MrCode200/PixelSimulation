import pygame

pygame.font.init()

# All Variables
WIN_WIDTH, WIN_HEIGHT = 1920, 1020
FPS = 120

NUM_OF_SLIMY_START = 15  # preferred
NUM_OF_FOOD_START = 100  # preferred
INFO_BOARD_ON = True  # preferred
#VISION_DRAW = False
SIMULATION_LVL = 2  # preferred

SLIMY_SPRITE_NUMBER = 14

SPRITE_SPEED = 0.3
SLIMY_VISION_STANDART = 45
SLIMY_START_ENERGY = 300
SLIMY_ENERGY_CAP = 400

BAT_VISION_STANDART = 45

CYCLE_IN_FPS = 0
CYCLE = 0
ENERGY_SLIMY = 0
ENERGY_FOOD = 0
ENERGY_REPRODUCTION = 0
TOTAL_SLIMY = 0
BAT_ENERGY = 0

IBF_COLOR = (0, 0, 0)

ICON_DNA = pygame.image.load("Assets/DNA.ico")
FONT = pygame.font.SysFont('Grand9K Pixel Regular', 10)

SLIMY_GROUP = pygame.sprite.Group()
FOOD_GROUP = pygame.sprite.Group()
BAT_GROUP = pygame.sprite.Group()

DATA_SPEED_SLIMY = []
DATA_VISION_SLIMY = []
DATA_CYCLE_SLIMY = []

DATA_SPEED_BAT = []
DATA_VISION_BAT = []
DATA_CYCLE_BAT = []

# NY #MAGIC
# Infinite:
# NUM_OF_SLIMY_START = 15  # preferred
# NUM_OF_FOOD_START = 120  # preferred
# generate food per cycle 15
