from pygame import *
from random import randint

finish = True
win_widht = 700
win_height = 500
game = True
clock = time.Clock()
FPS = 60
get_mouse_pos = 0
font.init()
font1 = font.SysFont('Arial',80)
win = font1.render('YOU WIN',True,(255,255,255))
lose = font1.render('YOU LOSE', True,(255,255,255))
draw = font1.render('DRAW', True,(255,255,255))
#Создание окна игры
window = display.set_mode((win_widht, win_height))
display.set_caption("Пинг-понг")
background = transform.scale(image.load('background.jpg'), (win_widht, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,player_speed_y):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.speed_y = player_speed_y

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def update_rock(self):
        keys = key.get_pressed()
        if keys[K_s]:
            variant_player = 1
            return variant_player

    def update_paper(self):
        keys = key.get_pressed()
        if keys[K_a]:
            variant_player = 2
            return variant_player

    def update_knife(self):
        keys = key.get_pressed()
        if keys[K_d]:
            variant_player = 3
            return variant_player


# if self.rect.x == get_mouse_pos and self.rect.y == get_mouse_pos:
#Экземпляры классов
rock = GameSprite('asteroid.png', 400, 200, 65, 80, 10,2)
paper = GameSprite('asteroid.png', 400, 100, 65, 80, 10,2)
knife = GameSprite('asteroid.png', 400, 300, 65, 80, 10,2)
while game:
    # Сделать завешение игры по нажатию крестика
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish or lose !=1:
        window.blit(background, (0, 0))
        rock.update_rock()
        paper.update_paper()
        knife.update_knife()

        rock.reset()
        paper.reset()
        knife.reset()
        variant_robot = randint(1,3)

        #Тут будет происходить сравнение с ботом
        if variant_player == 1:
            if variant_robot == 1:
                window.blit(draw, (0, 0))
            if variant_robot == 2:
                window.blit(lose, (0, 0))
            if variant_robot == 3:
                window.blit(win, (0, 0))

        if variant_player == 2:
            if variant_robot == 1:
                window.blit(win, (0, 0))
            if variant_robot == 2:
                window.blit(draw, (0, 0))
            if variant_robot == 3:
                window.blit(lose, (0, 0))

        if variant_player == 3:
            if variant_robot == 1:
                window.blit(lose, (0, 0))
            if variant_robot == 2:
                window.blit(win, (0, 0))
            if variant_robot == 3:
                window.blit(draw, (0, 0))
        
    display.update()
    time.delay(FPS)
