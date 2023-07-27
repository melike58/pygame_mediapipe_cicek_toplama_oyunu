import pygame
import random
import time
import image
from settings import *

class Flower:
    def __init__(self):
        
        random_size_value = random.uniform(FLOWER_SIZE_RANDOMIZE[0], FLOWER_SIZE_RANDOMIZE[1])
        size = (int(FLOWER_SIZES[0] * random_size_value), int(FLOWER_SIZES[1] * random_size_value))
        
        moving_direction, start_pos = self.define_spawn_pos(size)
        
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load("Assets/flower/2.png", size=size, flip=moving_direction=="right")]
        
        self.current_frame = 0
        self.animation_timer = 0


    def define_spawn_pos(self, size): #çiçeğin başlangıç konumunu ve hareket yönünü rastgele belirler
        vel = random.uniform(FLOWER_MOVE_SPEED["min"], FLOWER_MOVE_SPEED["max"]) #çiçeğin hızını temsil eder. min max arasında rastgele bir hız seçerek yapar.
        moving_direction = random.choice(("left", "right", "up", "down"))
        if moving_direction == "right": #başlangıç hareket yönünü temsil eder rastgele dört yönden birini seçer.
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT-size[1])) #başlangıç konumu
            self.vel = [vel, 0] #başlangıç hızı
        if moving_direction == "left":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [-vel, 0]
        if moving_direction == "up":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), SCREEN_HEIGHT+size[1])
            self.vel = [0, -vel]
        if moving_direction == "down":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), -size[1])
            self.vel = [0, vel]
        return moving_direction, start_pos


    def move(self): #belirli bi hız vektörüne göre hareket ettiren self.rect üzerinde olan çiçeğin sel.vel hız vektörüyle pozisyonunu günceller.
        self.rect.move_ip(self.vel)


    def animate(self): #çiçeğin görüntülerini bir animasyon dizisinde zaman içinde değiştirmek için kullanılır.
        t = time.time() # zamnan damgası
        if t > self.animation_timer: #bir sonraki çerçeve ne zaman geçiceğini hesaplar
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images)-1:
                self.current_frame = 0


    def draw_hitbox(self, surface): #çarpışma kutusunu çizer
        pygame.draw.rect(surface, (200, 60, 0), self.rect)



    def draw(self, surface): 
        self.animate() #çiçeğin animasyonunu yönetir
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)


    def picker(self, flovers): #el ile bir çiçeği seçip topladığını temsil eder
        flovers.remove(self) #bellirli bir çiçeğin seçildipini ve onun kaldırıldığını toplandığını temsil eder
        return 1 #1 ile çiçek toplamanın başarılı olduğunu söyler.
