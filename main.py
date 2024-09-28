import pygame
import json
import sim_function as sf
import variables as v

pygame.init()

# Create Window
WIN = pygame.display.set_mode((v.WIN_WIDTH, v.WIN_HEIGHT))
pygame.display.set_caption("Pixels Life")
pygame.display.set_icon(v.ICON_DNA)
clock = pygame.time.Clock()

"""#Input for Simulation
print("To set to prefered go to main.py and comment from line 14 to 24")
v.NUM_OF_SLIMY_START = int(input("Number of Slimy Simulation starts: "))
v.NUM_OF_FOOD_START = int(input("Number of food per cycle: "))
v.INFO_BOARD_ON = input("Info board on? y/n: ")
#v.SIMULATION_LVL = int(input("Simulation level (0:Fast, 1:Visualized, 2:Animation) #0 and 1 doesn't work yet: "))

if v.INFO_BOARD_ON == "y" or v.INFO_BOARD_ON == "":
    v.INFO_BOARD_ON = True
else:
    v.INFO_BOARD_ON = False"""

# Create Sprite/Slimy
sf.generate_slimy(v.NUM_OF_SLIMY_START)
sf.generate_food(v.NUM_OF_FOOD_START)
sf.generate_bat(30)


# Main
def main():
    run = True
    while run:
        clock.tick(v.FPS)

        for event in pygame.event.get():  # All Events
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.time.wait(3000)

                if event.key == pygame.K_p:
                    with open("data/data_slimy.json", "w") as f:
                        json.dump(v.DATA_CYCLE_SLIMY + v.DATA_SPEED_SLIMY + v.DATA_VISION_SLIMY, f)
                    with open("data/data_bat.json", "w") as f:
                        json.dump(v.DATA_CYCLE_BAT + v.DATA_SPEED_BAT + v.DATA_VISION_BAT, f)
                    pygame.quit()

        # for num_of_slimy in v.SLIMY_GROUP.sprites():
        #    print(num_of_slimy.energy) 
        # print(len(v.SLIMY_GROUP))
        sf.draw(WIN)


if __name__ == "__main__":
    main()
