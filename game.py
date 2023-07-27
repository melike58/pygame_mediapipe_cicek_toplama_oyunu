import pygame
import time
import random
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from flower import Flower
from bee import Bee
import cv2
import ui

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()

        
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["slap"] = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
        self.sounds["slap"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"Assets/Sounds/screaming.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)


    def reset(self): 
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.insects = []
        self.insects_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()


    def spawn_insects(self):
        t = time.time()
        if t > self.insects_spawn_timer:
            self.insects_spawn_timer = t + FLOWER_SPAWN_TIME

            nb = (GAME_DURATION-self.time_left)/GAME_DURATION * 100  / 2  
            if random.randint(0, 100) < nb:
                self.insects.append(Bee())
            else:
                self.insects.append(Flower())

            
            if self.time_left < GAME_DURATION/2:
                self.insects.append(Flower())

    def load_camera(self):
        _, self.frame = self.cap.read()


    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)

    def draw(self):
        
        self.background.draw(self.surface)
        
        for insect in self.insects:
            insect.draw(self.surface)
        
        self.hand.draw(self.surface)
        
        ui.draw_text(self.surface, f"Puan : {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))
        
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] 
        ui.draw_text(self.surface, f"Kalan Süre : {self.time_left}", (SCREEN_WIDTH//2, 5),  timer_text_color, font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255))


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)



    def update(self):

        self.load_camera()
        self.set_hand_position()
        self.game_time_update()

        self.draw()

        if self.time_left > 0:
            self.spawn_insects()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            print("Eller kapalı", self.hand.left_click)
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()
            self.score = self.hand.picker_flower(self.insects, self.score, self.sounds)
            for insect in self.insects:
                insect.move()

        else: 
            if ui.button(self.surface, 540, "Devam Et", click_sound=self.sounds["slap"]):
                return "menu"


        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
