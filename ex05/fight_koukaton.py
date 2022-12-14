import pygame as pg
import random
import sys
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

class Screen:
    def __init__(self, title, wh, img_path):

        pg.display.set_caption(title) #nigerokoukatonn
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path) #fig/pg_bg.jpg
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


def load_image(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()


class Bird:

    key_delta = {
        pg.K_UP:     [0, -1],
        pg.K_DOWN:   [0, +1],
        pg.K_RIGHT:  [+1, 0],
        pg.K_LEFT:   [-1, 0]
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path) #"fig/6.png"
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


class Explosion(pg.sprite.Sprite): #対応する画像の爆破

    defaultlife = 12
    animcycle = 3
    images = []

    def __init__(self, actor):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy) 
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1.3
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1.3
    return yoko, tate


def main():
    clock =pg.time.Clock()
    # 練習１
    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg")

    # 練習３
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    kkt.update(scr)

    # 練習５
    bkd_list = []
    bkd_color_list = [(255, 0, 0), (0, 255, 0,), (0, 0, 255), 
                      (0, 0, 1), (255, 255, 255)]
    for i in range(5):
        sum = random.randint(0,4)
        bkd = Bomb(bkd_color_list[sum], i*10, (+1, +1), scr)
        bkd_list.append(bkd)
    # 練習２
    img = load_image("explosion1.gif")
    Explosion.images = [img, pg.transform.flip(img, 1, 1)]
    bombs = pg.sprite.Group()
    birds = pg.sprite.Group()
    Bird.containers = birds, all
    Bomb.containers = bombs, all
    Explosion.containers = all

    while True:
        scr.blit() 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        for i in range(5):
            bkd_list[i].update(scr)
            if kkt.rct.colliderect(bkd_list[i].rct):
                pg.time.wait(500)
                return
            #for j in range(5):
            #   if i is j:
            #       None
            #   else:
            #       if bkd_list[i].rct.colliderect(bkd_list[j].rct):

        # for bomb in pg.sprite.spritecollide(birds, bombs, 1):
        #     Explosion(birds)
        #     Explosion(bomb)
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()