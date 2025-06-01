import pygame as pg
pg.font.init()
WIN_WIDTH = 500
WIN_HEIGHT = 500
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRAY = (100,100,100)
BLACK = (0,0,0)
bg = BLACK
mw = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pg.time.Clock()
font = pg.font.SysFont("Arial", 40)

class Game():
    count_pl_1 = 0
    count_pl_2 = 0
    run = True

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
        if self.rect.x <= 0:
            self.dirrect_x *= -1
            game.count_pl_2 += 1
            count_down_pl_2.set_text("Счёт: " + str(game.count_pl_2))
        if self.rect.x >= WIN_WIDTH - self.rect.width:
            self.dirrect_x *= -1
            game.count_pl_1 +=1
            count_down_pl_1.set_text("Счёт: " + str(game.count_pl_1))
        self.rect.x += self.speed * self.dirrect_x
        self.rect.y += self.speed * self.dirrect_y

class Area():
    def __init__(self,x=0,y=0,width=10,height=10,color=bg):
        self.rect = pg.Rect(x,y,width,height)
        self.fill_color = color

    #def fill(self):
        #pg.draw.rect(mw,self.fill_color,self.rect)

class Label(Area):
    def __init__(self,text,x=0,y=0,width=10,height=10,bg_color=bg,fsize=12, text_color=BLACK,border_color=BLUE):
        super().__init__(x=x,y=y,width=width,height=height,color=bg_color)
        self.text_color = text_color
        self.text = text
        self.fsize = fsize
        self.border_color = border_color
        self.set_text(text,fsize=fsize, text_color=text_color)
        self.text_draw_border()
    
    def set_text(self,text,fsize=None, text_color=None):
        if fsize is None:
            fsize = self.fsize
        if text_color is None:
            text_color = self.text_color
        self.text = text
        self.fsize = fsize
        self.image = pg.font.Font(None,fsize).render(text, True, text_color)

    def draw(self,shift_x=0, shift_y=0):
        pg.draw.rect(mw,self.fill_color,self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    
    def text_draw_border(self,border_color=BLUE):
        pg.draw.rect(mw,self.border_color,self.rect,10)
    
    def color_change(self,text_color):
        self.text_color = text_color

game = Game()
player_1 = Player("racket.png",10,100,4,50,150,pg.K_w,pg.K_s)
player_2 = Player("racket.png",440,200,4,50,150)
ball = Ball("tenis_ball.png",440,200,4,50,50)
count_down_pl_1 = Label("Счёт: 0", 20, 20, 140, 30, bg_color = BLACK, text_color=GRAY,fsize = 50)
count_down_pl_2 = Label("Счёт: 0", 350, 20, 140, 30, bg_color = BLACK, text_color=GRAY,fsize = 50)

while game.run == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game.run = False

    if game.count_pl_1 >= 10 or game.count_pl_2 >= 10:
        if game.count_pl_1 >= 9:
            count_down_pl_1.color_change(GREEN)
        if game.count_pl_2 >= 9:
            count_down_pl_2.color_change(GREEN)
        if game.count_pl_1 >= 19:
            count_down_pl_1.color_change(BLUE)
        if game.count_pl_2 >= 19:
            count_down_pl_2.color_change(BLUE)
        if game.count_pl_1 >= 29:
            count_down_pl_1.color_change(RED)
        if game.count_pl_2 >= 29:
            count_down_pl_2.color_change(RED)

    count_down_pl_1.draw()
    count_down_pl_2.draw()

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