import pygame

WINDOW_NAME = "ÇİÇEK TOPLAMA"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90 #oyunun görüntü akışının hızı
DRAW_FPS = True #FPS değeri ekranda gösterilsin demek

BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80) #ELin etkileşim alanunı belirleyen görünmez kutudur
FLOWER_SIZES = (50, 38)
FLOWER_SIZE_RANDOMIZE = (1,2) #çiçeğin orjinal boyutu üzerinden 1-2 kat arası boyutlarda olabilir
BEE_SIZES = (50, 50)
BEE_SIZE_RANDOMIZE = (1.2, 1.5)

DRAW_HITBOX = False #öğelerin hitboxı görünmesin diye false

ANIMATION_SPEED = 0.015

GAME_DURATION = 60 #oyun süresi
FLOWER_SPAWN_TIME = 1 #her saniyede bir yeni çiçek oluşturur
FLOWER_MOVE_SPEED = {"min": 1, "max": 5} #çiçeklerin hareket hızını belirler
BEE_PENALITY = 1 #Arıya dokunduğunda 1 puan azaltır

COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (229, 9, 229), "second":  (229, 9, 229),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} 

MUSIC_VOLUME = 0.16 #müzik sesinin seviyesi
SOUNDS_VOLUME = 1


pygame.font.init() #kütüphaneyi başlatmış olduk
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 40)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
