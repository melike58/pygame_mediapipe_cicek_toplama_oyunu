import pygame
import sys
from settings import *
from background import Background
import ui


class Menu: #oyunun menü kısımlarını temsil eden sınıftır.
    def __init__(self, surface): #sınıfın başlatıcı metodudur.surface menünün ögelerinin çizileceği yüzey,
        self.surface = surface
        self.background = Background() 
        self.click_sound = pygame.mixer.Sound(f"Assets/Sounds/slap.wav") #arkaplan ve tıklama sesi için gerekli nesneler oluşturulur. çünkü bu başlatıcı


    def draw(self): #menüyü ekrana çizen metot.
        self.background.draw(self.surface)
        
        ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 120), COLORS["title"], font=FONTS["big"], #draw_text metinleri çizer
                    shadow=True, shadow_color=(255,255,255), pos_mode="center")


    def update(self): #menüyü güncelleyen ve tıklamaları algılayan metottur.
        self.draw()
        if ui.button(self.surface, 320, "BAŞLA", click_sound=self.click_sound):
            return "game"

        if ui.button(self.surface, 320+BUTTONS_SIZES[1]*1.5, "ÇIKIŞ", click_sound=self.click_sound):
            pygame.quit()
            sys.exit()
