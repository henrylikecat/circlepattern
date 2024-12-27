import pgzrun
WIDTH=800
HEIGHT=800
TITLE="circlepattern"
def draw():
    screen.fill("white")
    r=65
    for i in range(20):
        screen.draw.circle((400,400), r, (255, 0, 0))
        r+=10
def update():
    pass
pgzrun.go()