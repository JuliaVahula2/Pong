from pygame import*

class GameSprite(sprite.Sprite):
     def __init__(self,player_image,player_x, player_y, pleyer_speed,width, height):
         supper().__init__()
         self.image=tranform.scale(image.player_image),(width, height))
         self.rect=self.image.get_rect()
         self.x=player_x
         self.y=player_y
         self.speed=player_speed
     def reset (self):
         mw.blit(self.image,(self.rect.x,self.rect.y))
f


width=600
height=600


mw=dissplay.set_mode((width, height))p
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
