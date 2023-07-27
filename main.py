import pygame
import sys
import os
from settings import *
from game import Game
from menu import Menu

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,32) #pencerenin tırnak içind everilen ankahtara bir değer atıyarak pencerenin ekran üzerindeki başlangıç koordinatları belirlenir.
pygame.init()
pygame.display.set_caption(WINDOW_NAME) #penverenin adını ayarlar
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32) 

mainClock = pygame.time.Clock() #oyun zamanını kontrol eder

fps_font = pygame.font.SysFont("coopbl", 22)

pygame.mixer.music.load("Assets/Sounds/Komiku_-_12_-_Bicycle.mp3")
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1)
state = "menu" #oyunun başlangıç durmunu menu sayfası olarak ayarlar

game = Game(SCREEN) #oyun içeriğini yönetir
menu = Menu(SCREEN) #menü kısmını yönetir

def user_events(): #kullanıcı etkileşimlerini işler
    for event in pygame.event.get(): #klavye girişleri, fare tıklamaları, pencere kapatma  gini kullanıcı etkileşimlerini yönetir.
        if event.type == pygame.QUIT: #oyun penceresini kaptırsa oyun kapanır
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: #klavyeye basarsa kullanıcı
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    global state
    if state == "menu":
        if menu.update() == "game": #oyunu başlat düğmesine tıklamışsa kullanıcı oyun durumunu game olarak değiştirir 
            game.reset() 
            state = "game"
    elif state == "game":
        if game.update() == "menu": #kullanıcı menüye dönmek istiyorsa
            state = "menu"
    pygame.display.update()
    mainClock.tick(FPS) #oyun döngüsünün hızınıu sınırlar



while True: #oyunun sürekli çalışmasını kullanıcı etkileşimlerini ve oyun içeriğinin güncellemesine ve ekranda fps değerinin görülmesine izin verir.

    user_events()

    update()

    if DRAW_FPS:
        fps_label = fps_font.render(f"FPS: {int(mainClock.get_fps())}", 1, (255,200,20))
        SCREEN.blit(fps_label, (5,5))
