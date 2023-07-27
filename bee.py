import pygame
import random
import image
from settings import *
from flower import Flower

class Bee(Flower):
    def __init__(self): #Arı sınıfı çağırılınca arının özellikleirni tanımlar.
        
        random_size_value = random.uniform(BEE_SIZE_RANDOMIZE[0], BEE_SIZE_RANDOMIZE[1])#rastegele lisetnin içinden en küçük ve ne büyük değer arasından arının boyutunu belirler. 
        size = (int(BEE_SIZES[0] * random_size_value), int(BEE_SIZES[1] * random_size_value))
        moving_direction, start_pos = self.define_spawn_pos(size) #arının başlangıç hareket yönünü temsil eden dizedir.
        
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4) #arının dörtgen boyutunu belirler
        self.images = [image.load(f"Assets/bee/{nb}.png", size=size, flip=moving_direction=="right") for nb in range(1, 7)] #arı dosyalrının 1den 6ya kadar 6dahil isimlendirir ve load ile bu resimelri yükleriz 
        self.current_frame = 0 #arının şuanki bulunduğu çerçeve
        self.animation_timer = 0 #
        

    def picker(self, flowers): #çiçek seçim işlemidir. flowers listesindeki çiçeklerden birini seçer. arıyı seçtiğinde eksi puanı bee-penality ile eksiltir. 
        flowers.remove(self)
        return -BEE_PENALITY #- ceza değeri
