import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img, True, False)
    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton, True, False)
    kk_rct = koukaton.get_rect()    # こうかとんrectの抽出
    kk_rct.center = 300, 200        # こうかとんの中心を300, 200に設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return


        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_flip, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img_flip, [-x+4800, 0])
        screen.blit(koukaton, kk_rct)
        kk_rct.move_ip((-1, 0)) # こうかとんが左に移動する
        
        key_lst = pg.key.get_pressed() #全キーの押下状態を取得
        kk_x = 0
        kk_y = 0
        if key_lst[pg.K_UP]:
            kk_x, kk_y = 0, -1
        elif key_lst[pg.K_DOWN]:
            kk_x, kk_y = 0, 1
        elif key_lst[pg.K_LEFT]:
            kk_x, kk_y = -1, 0
        elif key_lst[pg.K_RIGHT]:
            kk_x, kk_y = 2, 0

        kk_rct.move_ip(kk_x, kk_y)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()