import pygame
import random

#main characters : Wall, Food, Player


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, bg_color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


class Player(pygame.sprite.Sprite):

    #object of PLayer : (blinky.png)
    def __init__(self, x, y, role_image_path):
        pygame.sprite.Sprite.__init__(self)
        self.role_name = role_image_path.split('/')[-1].split('.')[0]
        self.base_image = pygame.image.load(role_image_path).convert()
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.prev_x = x
        self.prev_y = y

        self.base_speed = [30, 30]
        self.speed = [0, 0]

        self.is_move = False

        self.tracks = []
        self.tracks_loc = [0, 0]

        #[[2, 3], [], []]
        #direction = [2,3]

    def changeSpeed(self, direction ):
        if direction[0] < 0:
            self.image = pygame.transform.flip(self.base_image, True, False)

        if direction[0] > 0:
            self.image = self.base_image.copy()

        if direction[1] < 0:
            self.image = pygame.transform.rotate(self.base_image, 90)

        if direction[1] > 0:
            self.image = pygame.transform.rotate(self.base_image, -90)


        self.speed = [direction[0] * self.base_speed[0], direction[1] * self.base_speed[1]]

        return self.speed

    def update(self, wall_sprites, gate_sprites):
        """move your character"""
        if not self.is_move:
            return False
        x_prev = self.rect.left
        y_prev = self.rect.top

        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]


        #collision code
        is_collide = pygame.sprite.spritecollide(self, wall_sprites, False)
        if gate_sprites is not None:
            if not is_collide:
                is_collide = pygame.sprite.spritecollide(self, gate_sprites, False)

        if is_collide:
            self.rect.left = x_prev
            self.rect.top = y_prev

            return False
        return True



    def randomDirection(self):
        return random.choice([[-0.5, 0], [0.5, 0], [0, 0.5], [0, -0.5]])




















