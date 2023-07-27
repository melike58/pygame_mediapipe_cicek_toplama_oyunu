import pygame
import image
from settings import *
from hand_tracking import HandTracking
import cv2

class Hand:
    def __init__(self):
        self.orig_image = image.load("Assets/hand.png", size=(HAND_SIZE, HAND_SIZE))#orjinal boyuttunda yükler el resmini ve belirtilen boyuta ölçeklendirir.
        self.image = self.orig_image.copy() #el resminin koyasıdır .
        self.image_smaller = image.load("Assets/hand.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1]) #hitboxu temsil eder
        self.left_click = False


    def follow_mouse(self): #el simülasyonunu kullanıcının fare konumuna göre hareket ettirir.
        self.rect.center = pygame.mouse.get_pos()

    def follow_mediapipe_hand(self, x, y): #el simülasyonunu el koordinatına göre hareket ettirir.El takip sisteminden aldığı koordinatlara göre hareket ettirir.
        self.rect.center = (x, y)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)


    def draw(self, surface): #el resmşni ekranda çizer.   
        image.draw(surface, self.image, self.rect.center, pos_mode="center")

        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def on_flower(self, flowers): #çiçekleri tespit eder ve çiçeklere temeas eden el simülasyonunu bulur.El simülasyonun self.rect'i ile çiçeklerin çarpışma kutuları arasında çarpışma olup olmadığını tespit eder. 
        return [flower for flower in flowers if self.rect.colliderect(flower.rect)] #çarpışma kutularının çarpışıp çarpışmadığını kontrol eder ve true false değeri döndürür.
                #insect kontrol edilecek çiçekelri içerir.

    def picker_flower(self, flowers, score, sounds): #çarpışma gerçekleştiyse ve farenin sol clicine basıldıysa çiçeği toplar ve puanı günceller ve ses efekti verir.
        if self.left_click: 
            for flower in self.on_flower(flowers):
                flower_score = flower.picker(flowers)
                score += flower_score
                sounds["slap"].play()
                if flower_score < 0:
                    sounds["screaming"].play()
        else:
            self.left_click = False
        return score
