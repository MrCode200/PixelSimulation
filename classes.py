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

        self.VAR_movement_counter = 0

        # Perks and info
        self.energy = v.SLIMY_START_ENERGY
        self.speed = SPEED
        self.radius = SLIMY_VISION  # VISION couldn't change name to radius

        self.vision_color = (128, 128, 128)

        # create rect for object
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def collide(self):
        # check if food is in vision with a collidide circle
        vision_collide = pygame.sprite.spritecollide(self, v.FOOD_GROUP, False, pygame.sprite.collide_circle)
        enemy_collide = pygame.sprite.spritecollide(self, v.BAT_GROUP, False, pygame.sprite.collide_circle)
        # check if food can be eaten with a collidide circle
        food_reach_collide = pygame.sprite.spritecollide(self, v.FOOD_GROUP, True,
                                                         pygame.sprite.collide_circle_ratio(0.2))

        # if vision_collide is empty just do random movement

        if enemy_collide != [] and self.energy > 65:
            self.vision_color = (128, 0, 0)
            if enemy_collide[0].rect.x > self.rect.x and self.rect.midleft[0] < 0:
                self.rect.x -= self.speed
            elif self.rect.midright[0] < v.WIN_WIDTH:
                self.rect.x += self.speed
            if enemy_collide[0].rect.y > self.rect.y and self.rect.midbottom[1] < 0:
                self.rect.y -= self.speed
            elif self.rect.midtop[1] < v.WIN_HEIGHT:
                self.rect.y -= self.speed

        elif vision_collide == []:
            self.vision_color = (128, 128, 128)
            self.movement()

        # else go towards the food
        else:
            # check if food got eaten
            if food_reach_collide != []:
                self.energy += food_reach_collide[0].energy

            # move towards food
            if vision_collide[0].rect.x > self.rect.x and self.rect.midright[0] < v.WIN_WIDTH:
                self.rect.x += self.speed
            elif self.rect.midleft[0] > 0:
                self.rect.x -= self.speed
            if vision_collide[0].rect.y > self.rect.y and self.rect.midtop[1] > 0:
                self.rect.y += self.speed
            elif self.rect.midbottom[1] < v.WIN_HEIGHT:
                self.rect.y -= self.speed
            self.vision_color = (0, 100, 0)

    # the Binary Fission of slimes and slime energy monitor
    def binary_fission(self):
        if self.energy >= v.SLIMY_ENERGY_CAP:
            sf.generate_slimy(2, self.rect.x, self.rect.y, self.speed, self.radius)
            v.SLIMY_GROUP.remove(self)
        elif self.energy <= 0:
            v.SLIMY_GROUP.remove(self)
        self.energy -= 0.15 * (self.speed * 2 + self.radius / 20)

    def movement(self):
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
        elif self.rect.midbottom[1] < v.WIN_HEIGHT:
            self.rect.y += self.speed

    # Update the sprite currrent picture
    def update(self):

        self.current_sprite += self.sprite_speed  # self.sprite_speed * self.speed

        # Check so the current_sprite array isn't bigger than the sprite number 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.collide()

        # load next sprite and call all functions
        self.image = self.sprites[int(self.current_sprite)]
        self.binary_fission()


class bat(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__()

        self.egg_sprites = sf.create_bat_sprite(True)
        self.sprites = sf.create_bat_sprite(False)
        self.current_sprite = 0
        self.image = self.egg_sprites[int(self.current_sprite)]

        self.speed = speed
        self.energy = 750
        self.radius = 75
        self.movement_counter = 0

        self.hatched = False
        self.sprite_cycle = 0

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.bat_animation()

        if self.hatched:
            self.collide()
            self.reproduce()

    def bat_animation(self):
        #check if bat is hatche every cycle
        if not self.hatched and self.sprite_cycle == 60:
            #update sprite img
            self.image = self.egg_sprites[int(self.current_sprite)]
            self.current_sprite += 1
            self.sprite_cycle = 0
        # if the sprite shows bat has hatched the self.hatched = True
            if self.current_sprite >= len(self.egg_sprites):
                self.hatched = True

        #add to sprite_cycle in context (egg)
        elif not self.hatched:
            self.sprite_cycle += 1

        #if the egg hatched create animation
        elif self.sprite_cycle == 3:
            self.sprite_cycle = 0
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]
        else:
            self.sprite_cycle += 1

    def collide(self):
        vision_collide = pygame.sprite.spritecollide(self, v.SLIMY_GROUP, False, pygame.sprite.collide_circle)
        reach_collide = pygame.sprite.spritecollide(self, v.SLIMY_GROUP, True, pygame.sprite.collide_circle_ratio(0.2))

        if vision_collide == []:
            self.movement()

        else:
            if vision_collide[0].rect.x > self.rect.x:
                self.rect.x += self.speed
            elif vision_collide[0].rect.x < self.rect.x:
                self.rect.x -= self.speed
            if vision_collide[0].rect.y > self.rect.y:
                self.rect.y += self.speed
            if vision_collide[0].rect.y < self.rect.y:
                self.rect.y -= self.speed

            if reach_collide != []:
                self.energy += round(reach_collide[0].energy, 2)

    def movement(self):
        if self.movement_counter == 0:
            self.bat_radint = random.randint(1, 4)
        if self.movement_counter == 32:
            self.movement_counter = 0
        else:
            self.movement_counter += 1

        if self.bat_radint == 1 and self.rect.midright[0] < v.WIN_WIDTH:
            self.rect.x += self.speed
        elif self.bat_radint == 2 and self.rect.midleft[0] > 0:
            self.rect.x -= self.speed
        elif self.bat_radint == 3 and self.rect.midtop[1] > 0:
            self.rect.y -= self.speed
        elif self.rect.midbottom[1] < v.WIN_HEIGHT:
            self.rect.y += self.speed

    def reproduce(self):
        if self.energy >= 1250:
            sf.generate_bat(1, self.rect.x, self.rect.y, self.speed)
            self.energy -= 1000
        elif self.energy <= 0:
            v.BAT_GROUP.remove(self)
        self.energy -= 0.1*(self.speed+self.radius/20)
        self.energy = round(self.energy, 2)



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
        if self.energy < 250:
            self.energy += 0.1
            self.image = pygame.transform.scale(pygame.image.load(self.IMAGE_VERSION),
                                                (self.energy / 4, self.energy / 4))
