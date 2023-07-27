import pygame
import image

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.display.set_caption("Game")
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

background = image.load("Assets/background.jpg",size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                        convert="default")


from flower import Flower
from bee import Bee
from hand import Hand

flower1 = Flower()
flower2 = Flower()
bee1 = Bee()
hand = Hand()

while True:

    image.draw(SCREEN, background, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), pos_mode="center")
    #image.draw(SCREEN, flower1.images[0], (452 , 235), pos_mode="center")
    #image.draw(SCREEN, flower2.images[0], (589 , 455), pos_mode="center")

    image.draw(SCREEN, hand.image, hand.rect, pos_mode="center")
    hand.follow_mouse()
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()



    pygame.display.update()