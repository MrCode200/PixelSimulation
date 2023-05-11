import pygame
import random
import variables as v
import sim_function as sf


class slimy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, SPEED, SLIMY_VISION):  # add SLIMY_WIDTH, SLIMY_HEIGHT, SPRITE
        super().__init__()

        # load in the sprites and prepare Sprites
        self.sprites = sf.create_jump_sprite_slime()
        self.current_sprite = 0
        self.sprite_speed = v.SPRITE_SPEED  # can be changed to 0.3 and deleted in variables
        self.image = self.sprites[self.current_sprite]
        self.is_animating = False

        self.VAR_movement_counter = 0

        # Perks and info
        self.energy = v.SLIMY_START_ENERGY
        self.speed = SPEED
        self.radius = SLIMY_VISION  # VISION couldn't change name to radius

        self.vision_color = (255, 255, 255)

        # create rect for object
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def collide(self):
        # check if food is in vision with a collidide circle
        vision_collide = pygame.sprite.spritecollide(self, v.FOOD_GROUP, False, pygame.sprite.collide_circle)
        # check if food can be eaten with a collidide circle
        food_reach_collide = pygame.sprite.spritecollide(self, v.FOOD_GROUP, True,
                                                         pygame.sprite.collide_circle_ratio(0.2))

        # if vision_collide is empty just do random movement
        if vision_collide == []:
            self.vision_color = (255, 255, 255)
            self.random_movement()

        # else go towards the food
        else:
            # check if food got eaten
            if food_reach_collide != []:
                self.energy += food_reach_collide[0].energy

            # move towards food
            if vision_collide[0].rect.center[0] > self.rect.center[0]:
                self.rect.x += self.speed
            elif vision_collide[0].rect.center[0] < self.rect.center[0]:
                self.rect.x -= self.speed
            if vision_collide[0].rect.center[1] > self.rect.center[1]:
                self.rect.y += self.speed
            elif vision_collide[0].rect.center[1] < self.rect.center[1]:
                self.rect.y -= self.speed
            self.vision_color = (255, 0, 0)

    # the Binary Fission of slimes and slime energy monitor
    def binary_fission(self):
        if self.energy >= v.SLIMY_ENERGY_CAP:
            sf.generate_slimy(2, self.rect.x, self.rect.y, self.speed, self.radius)
            v.SLIMY_GROUP.remove(self)
        elif self.energy <= 0:
            v.SLIMY_GROUP.remove(self)
        else:
            self.energy -= 0.1 * (self.speed * 2 + self.radius / 40)

    def animate(self):
        self.is_animating = True

    def random_movement(self):
        # Update random number for movement
        if self.VAR_movement_counter == 0:
            self.SLIMY_RADINT = random.randint(1, 4)
        # if sprite animation ended reset random movement
        if self.VAR_movement_counter == 39:
            self.VAR_movement_counter = 0
        # add to random movement 1 after 1 sprite
        else:
            self.VAR_movement_counter += 1

        # move depending on random number
        if self.SLIMY_RADINT == 1 and self.rect.midright[0] < v.WIN_WIDTH:
            self.rect.x += self.speed
        elif self.SLIMY_RADINT == 2 and self.rect.midleft[0] > 0:
            self.rect.x -= self.speed
        elif self.SLIMY_RADINT == 3 and self.rect.midtop[1] > 0:
            self.rect.y -= self.speed
        elif self.SLIMY_RADINT == 4 and self.rect.midbottom[1] < v.WIN_HEIGHT:
            self.rect.y += self.speed

    # Update the sprite currrent picture
    def update(self):

        if self.is_animating == True:

            self.current_sprite += self.sprite_speed  # self.sprite_speed * self.speed

            # Check so the current_sprite array isn't bigger than the sprite number 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            else:
                self.collide()

            # load next sprite and call all functions
            self.image = self.sprites[int(self.current_sprite)]
            self.binary_fission()


class one_eye_bat(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.image = pygame.image.load("None")
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        pass


class food(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        if random.randint(1, 5) == 1:
            self.IMAGE_VERSION = "Assets/Food2_Slimy.png"
            self.energy = 100
        else:
            self.IMAGE_VERSION = "Assets/Food_Slimy.png"
            self.energy = 60

        self.image = pygame.transform.scale(pygame.image.load(self.IMAGE_VERSION), (25, 25))

        self.food_cycle = 0
        self.growth_rate = 0.2

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        # Growth of food
        if self.energy < 500:
            self.energy += 0.1
            self.image = pygame.transform.scale(pygame.image.load(self.IMAGE_VERSION),
                                                (self.energy / 4, self.energy / 4))
