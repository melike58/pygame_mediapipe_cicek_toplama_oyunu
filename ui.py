import pygame
from settings import *

#metni yüzey üzerine çizen metin çizim işlevini tanımlar.
#surface :Metnin çizileceği yüzey, text :metin, pos :metnin konumu, pos_mode :metnin konum modu metnin sol üst köşesi
# shadow :metnin altına gölge ekelr ama burda false,    
def draw_text(surface, text, pos, color, font=FONTS["medium"], pos_mode="top_left", 
                shadow=False, shadow_color=(0,0,0), shadow_offset=2):
    label = font.render(text, 1, color)#text i render eder
    label_rect = label.get_rect() #label ın sınırlayıcı dörtgeni
    if pos_mode == "top_left": 
        label_rect.x, label_rect.y = pos
    elif pos_mode == "center":
        label_rect.center = pos

    if shadow: 
        label_shadow = font.render(text, 1, shadow_color)
        surface.blit(label_shadow, (label_rect.x - shadow_offset, label_rect.y + shadow_offset))

    surface.blit(label, label_rect) #label metnini dörtgenin belirtilen konumuna çizer.



def button(surface, pos_y, text=None, click_sound=None):
    rect = pygame.Rect((SCREEN_WIDTH//2 - BUTTONS_SIZES[0]//2, pos_y), BUTTONS_SIZES)#bir rect(dikdörtgen)oluşturup butonun konumunu ve sınırlarını temsil eder.
                                                                                     
    on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()): #fare imlecinin butonun üzerindemi diye bakıyor.
        color = COLORS["buttons"]["second"] #üzerindeyse eğer on_button=True olur ve rengi değişir.
        on_button = True
    else:
        color = COLORS["buttons"]["default"]

    pygame.draw.rect(surface, COLORS["buttons"]["shadow"], (rect.x - 6, rect.y - 6, rect.w, rect.h))
    pygame.draw.rect(surface, color, rect) 
    
    if text is not None:
        draw_text(surface, text, rect.center, COLORS["buttons"]["text"], pos_mode="center",
                    shadow=True, shadow_color=COLORS["buttons"]["shadow"])

    if on_button and pygame.mouse.get_pressed()[0]:  #on_button trueysa ve sol fare tuşu basılıysa(pygame.mouse.get_pressed()[0]) tıklama işlemi gerçekleşir
        if click_sound is not None: #none değilse tıklama sesi çalınır
            click_sound.play()
        return True
