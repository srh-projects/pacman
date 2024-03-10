import pygame
import Levels
import os
import sys

HEROPATH = os.path.join(os.getcwd(), 'resources/images/pacman.png')
BlinkyPATH = os.path.join(os.getcwd(), 'resources/images/Blinky.png')
ClydePATH = os.path.join(os.getcwd(), 'resources/images/Clyde.png')
InkyPATH = os.path.join(os.getcwd(), 'resources/images/Inky.png')
PinkyPATH = os.path.join(os.getcwd(), 'resources/images/Pinky.png')
FONTPATH = os.path.join(os.getcwd(), 'resources/font/ALGER.TTF')
SOUNDPATH = os.path.join(os.getcwd(), 'resources/sounds/bg.mp3')

def startGame(level, screen, font):
    clock = pygame.time.Clock()
    wall_sprites = level.setupWalls((0, 128, 0))
    gate_sprites = level.setupGate((255, 255, 255))

    hero_sprites, ghost_sprites = level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
    food_sprites = level.setupFood((255, 255, 0), (255, 255, 255))
    SCORE = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(-1)
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for hero in hero_sprites:
                        hero.changeSpeed([-1, 0])
                        hero.is_move = True

                elif event.key == pygame.K_RIGHT:
                    for hero in hero_sprites:
                        hero.changeSpeed([1, 0])
                        hero.is_move = True

                elif event.key == pygame.K_UP:
                    for hero in hero_sprites:
                        hero.changeSpeed([0, -1])
                        hero.is_move = True

                elif event.key == pygame.K_DOWN:
                    for hero in hero_sprites:
                        hero.changeSpeed([0, 1])
                        hero.is_move = True



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or \
                        event.key == pygame.K_DOWN:
                    hero.is_move= False

        screen.fill((0, 0, 0 ))


        for hero in hero_sprites:
            hero.update(wall_sprites, gate_sprites)

        hero_sprites.draw(screen)

        #lets see if we habve collision between our pacman and food

        for hero in hero_sprites:
            food_eaten = pygame.sprite.spritecollide(hero, food_sprites, True)

        SCORE += len(food_eaten)

        wall_sprites.draw(screen)
        gate_sprites.draw(screen)
        food_sprites.draw(screen)

        for ghost in ghost_sprites:
            if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
                ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0:2]) #(0, 1)
                ghost.tracks_loc[1] += 1
            else:
                if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                    ghost.tracks_loc[0] += 1

                else:
                    ghost.tracks_loc[0] = 0

                ghost.tracks_loc[1] = 0


            if ghost.tracks_loc[1] < ghost.tracks[ghost.tracks_loc[0]][2]:
                ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0:2])

            else:
                if ghost.tracks_loc[0] < len(ghost.tracks) - 1:
                    loc0 = ghost.tracks_loc[0] + 1

                else:
                    loc0 = 0

                ghost.changeSpeed(ghost.tracks[loc0][0:2])


            ghost.update(wall_sprites, None)


        ghost_sprites.draw(screen)


        score_text = font.render("Score: %s" %SCORE, True, (255, 0, 0))
        screen.blit(score_text, [10, 10])

        if pygame.sprite.groupcollide(hero_sprites, ghost_sprites, False, False):
            break

        pygame.display.flip()
        clock.tick(10)


def initialize():
    pygame.init()
    screen = pygame.display.set_mode([606, 606])
    return screen


def main(screen):
    pygame.mixer.init()
    pygame.mixer.music.load(SOUNDPATH)
    pygame.mixer.music.play(-1, 0.0)


    font = pygame.font.Font(FONTPATH, 18)
    for num_level in range(1, Levels.NUMLEVELS+1):
        if num_level == 1:
            level = Levels.Level1()
            startGame(level, screen, font)



if __name__ == "__main__":
    main(initialize())