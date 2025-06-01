import pygame as pg
WIN_WIDTH = 500
WIN_HEIGHT = 500
BLACK = (0,0,0)
bg = BLACK
mw = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
game = True

class GameSprite(pg.sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed, width, height, key_up = pg.K_UP, key_down = pg.K_DOWN):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(sprite_image), (width, height))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.key_up = key_up
        self.key_down = key_down
        self.dirrect_x = 1
        self.dirrect_y = 1
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
    def fill(self):
        pg.draw.rect(mw, bg, self.rect)

class Player(GameSprite):
    def update(self):
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[self.key_up] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys_pressed[self.key_down] and self.rect.y < WIN_HEIGHT - self.speed - self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if self.rect.colliderect(player_1.rect) or self.rect.colliderect(player_2.rect):
            self.dirrect_x *= -1
        if self.rect.y <= 0 or self.rect.y >= WIN_HEIGHT - self.rect.height:
            self.dirrect_y *= -1
        #Заменить на выйгрыш и проигрыш
        if self.rect.x <= 0 or self.rect.x >= WIN_WIDTH - self.rect.width:
            self.dirrect_x *= -1
        #!!!
        self.rect.x += self.speed * self.dirrect_x
        self.rect.y += self.speed * self.dirrect_y

player_1 = Player("racket.png",10,100,4,50,150,pg.K_w,pg.K_s)
player_2 = Player("racket.png",440,200,4,50,150)
ball = Ball("tenis_ball.png",440,200,4,50,50)

while game == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False

    player_1.fill()
    player_2.fill()
    ball.fill()

    player_1.update()
    player_2.update()
    ball.update()

    player_1.reset()
    player_2.reset()
    ball.reset()

    pg.display.update()
    clock.tick(60)