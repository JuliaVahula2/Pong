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

class Player(GameSprite):
     def update_r(self):
          key=key.get_pressed()
          if key[K_UP] and self.rect.y<0:
             self.rect.y-=self.speed
          if key[K_DOWN] and self.rect.y>widht-80:
               self.rect.y+=self.speed
     def update_l(self):
          def update_l(self):
          key=key.get_pressed()
          if key[K_W] and self.rect.y<0:
             self.rect.y-=self.speed
          if key[K_S] and self.rect.y>widht-80:
               self.rect.y+=self.speed

racket1=Player("racket.png", 50,200, 4,50,150)
racket2=Player("racket.png", 350,200, 4,50,150)

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
