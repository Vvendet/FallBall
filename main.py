from cmath import cos, sin
import pygame as pg
import math

from pyparsing import White
pg.init()

x = 1000
y = 500
janela = pg.display.set_mode((x,y))
pg.display.set_caption("Simulação")
fonte = pg.font.SysFont('arial',40,bold=True,italic = False)
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)
ctrl = False
c = 0
d = 0
t = 0
v = 0
xc, yc = [0,0]
ag = 9.8
ag2 = ag
e = 0.6
vd = 0
subindo = False
while True:
    
    vj = v + ag*t
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    mouse = pg.mouse.get_pos()
    posicio = mouse[0]
    posicio2 =mouse[1]
    pg.draw.line(janela, (255,255,255), (50-15,0), (50-15,y-50))
    pg.draw.line(janela, (255,255,255), (0,y-70), (x/2-60,y-70))

    if pg.mouse.get_pressed()[0] == 1 and mouse[0] < x/2 - 50 and mouse[0] >  50:
        if mouse[1] < y-100+14 - 12:
            if ctrl:
                ctrl = False
                c = 0
                t = 0
                v = 0.01
                ag = 9.8
                vd = 0
            else:
                ctrl = True
                xc, yc = [posicio, posicio2]

    if ctrl:
        
        pg.draw.rect(janela, (0,0,0), pg.Rect(50-12, 0, x/2-50+12, y-100+14))
        circle1 = pg.draw.circle(janela, (255, 0, 0), (xc, d), 12)
        c = (yc + v*t + (ag*t**2)/2 - y)
        d = c + y

        if (d>= y - 100):
            yc = y - 100
            vj = vj*(-1)
            ag2 = ag2*(-1)
            v = e*vj
            t = 0
    
        t += 0.05

    pg.display.update()
