import pygame

def load(img_path, size="default", convert="alpha", flip=False): #görüntüyü yüklemek için kullanılır.
    if convert == "alpha": #görüntüyü alpha kanalının değerini koruyararak dönüştürür. 
        img = pygame.image.load(img_path).convert_alpha()
    else:
        img = pygame.image.load(img_path).convert()

    if flip:
        img = pygame.transform.flip(img, True, False)

    if size != "default":
        img = scale(img, size)

    return img


def scale(img, size): #görüntüyü istenen boyutlarda yeniden boyutlandırır.
    return pygame.transform.smoothscale(img, size)


def draw(surface, img, pos, pos_mode="top_left"): #yüzeye görüntü çizmek için kullanılır.
    if pos_mode == "center":
        pos = list(pos)
        pos[0] -= img.get_width()//2
        pos[1] -= img.get_height()//2

    surface.blit(img, pos)
