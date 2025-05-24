import pygame as pg
mw = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > SPEED:
            self.rect.y -= SPEED
        if keys_pressed[K_DOWN] and self.rect.y < WIN_HEIGHT - SPEED - SPRITE_SIZE:
            self.rect.y += SPEED

while game == True:
    pg.display.update()
    clock.tick(60)