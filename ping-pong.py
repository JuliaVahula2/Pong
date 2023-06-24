from pygame import*
width=600
height=600


mw=dissplay.set_mode((width, height))
display.set_caption("Пін понг")
clock=time.Clock()


game=True
finish=False
FPS=60

while game:
    for e in event.get():
         if e.type==QUIT:
            game=False


  display.update()
clock.tick(FPS)