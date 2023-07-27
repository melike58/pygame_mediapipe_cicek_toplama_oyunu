import pygame
import image
from settings import *

class Background: #oyunun arka planını çizer
    def __init__(self): #başlatıcı metottur. bu sınıftan bir örnek oluşturulduğunda çağrılır.
        self.image = image.load("Assets/masal-diyari.webp", size=(SCREEN_WIDTH, SCREEN_HEIGHT), #arka plan resmini yükler 
                                convert="default")


    def draw(self, surface): #arka planı çizer. resim merkeze konumlandırılır.
        image.draw(surface, self.image, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), pos_mode="center")
