from pygame import *

window = display.set_mode((700,500))
display.set_caption('Забери Калаш!')

bg = transform.scale(image.load('background.jpg'),(700,500))

mixer.init()
mixer.music.load('Rust_-_Fishing_village_75860584.mp3')
mixer.music.play()

game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 615:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2, color_3, wall_x, wall_y, width, height):
        super().__init__()
        self.image = Surface((width,height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x , self.rect.y))

player = Player('еока.jpg', 5, 420, 4)
monster = Enemy('Джагер.jpg', 620, 280, 2)
final = GameSprite('Калаш.jpg', 580, 420, 0)

w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 80, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 680, 20, 10, 380)
w5 = Wall(154, 205, 50, 230, 110, 10, 380)
w6 = Wall(154, 205, 50, 325, 20, 10, 380)
w7 = Wall(154, 205, 50, 420, 110, 10, 380)
w8 = Wall(154, 205, 50, 520, 350, 10, 80)
w9 = Wall(154, 205, 50, 520, -25, 10, 300)


clock = time.Clock()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial', 70)
win = font.render("Еее калаш", True, (0,255,0))
lose = font.render("Просрал калаш:(", True, (0,255,0))

walls = [w1, w2, w3, w4, w5, w6, w7, w8, w9]
finish = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(bg, (0,0))
        player.reset()
        monster.reset()
        final.reset()
        player.update()
        monster.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()

        if sprite.collide_rect(player, final):
            finish = True
            money.play()
            window.blit(win, (200,200))
        if sprite.collide_rect(player, monster):
            finish = True
            kick.play()
            window.blit(lose, (200,200))
        for i in walls:
            if sprite.collide_rect(player, i):
                finish = True
                kick.play()
                window.blit(lose, (200,200))
    
    display.update() 
    time.delay(10)   