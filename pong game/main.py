import pygame 
import os 
pygame.init()
pygame.mixer.init()
pygame.font.init()
textfont = pygame.font.SysFont("monospace" , 50)

hit_sound = pygame.mixer.Sound("Assets/sound1.wav")
width,height = 900,600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong Game")
run = True
fps = 60
lx,ly = 0,0
ry= 0
rx =880
bx,by = 442,300
ballsx = 2
ballsy = 2
lscore = 0
rscore = 0
padlecolor = (92, 225, 230)
border = pygame.Rect((width//2) + 5,0,5,600)
white =(255,255,255)
lpdl =pygame.Rect(lx,ly,20,120)
rpdl = pygame.Rect(rx,ry,20,120)
ball_rect = pygame.Rect(bx, by, 20, 20)
def leftpadle():
  
  pygame.draw.rect(screen,padlecolor,lpdl)
  
def rightpadle():
  
  pygame.draw.rect(screen,padlecolor,rpdl)
  
def ball():
    pygame.draw.rect(screen, white, ball_rect,border_radius=20)  # Draw the ball rectangle
   #  screen.blit( ball_rect)  # Blit the ball image onto the rectangle



def drawer():
 screen.fill("#0A1331")
 pygame.draw.rect(screen,white,border)


 leftpadle()
 rightpadle()
 ball()
while run :
 clock.tick(fps)
#  making the movement of the ball and checking collision 
 ball_rect.x +=ballsx
 ball_rect.y -=ballsy
 lscoretxt = textfont.render(f"{lscore}", 1,(255,255,255))
 screen.blit(lscoretxt,(370,0))
 rscoretxt = textfont.render(f"{rscore}",1,(255,255,255))
 screen.blit(rscoretxt,(500,0))
# upper collision 
 if  ball_rect.y < 0 :
    hit_sound.play()
    ballsy = -ballsy
    
    
# lower collision 
 if ball_rect.y >580:
    hit_sound.play()
    ballsy = -ballsy
    
    
# score for game 
 if ball_rect.x <0 :
    ball_rect.x = 450 
    ball_rect.y = 300
    rscore +=1
    ballsx = -ballsx
    ballsy = - ballsy
    
 if ball_rect.x  >900 :
   ball_rect.x = 450 
   ball_rect.y = 300
   lscore+=1
   ballsx = -ballsx
   ballsy = - ballsy
   

 # collison with paddles 
 if ball_rect.colliderect(rpdl):
    hit_sound.play()
    ballsx +=2
    ballsy+=2
    ballsx = -ballsx
 if ball_rect.colliderect(lpdl):
    hit_sound.play()
    ballsx +=2
    ballsy+=2
    
    ballsx = -ballsx

    
    
 

 def main():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]and rpdl.y<480:
       rpdl.y +=6
    if keys[pygame.K_UP]and rpdl.y>0:
       rpdl.y -=6
    if keys[pygame.K_w]and lpdl.y>0:
       lpdl.y-=6
    if keys[pygame.K_s]and lpdl.y<480:
       lpdl.y+=6

   
       

          
 pygame.display.update()
 drawer()
 main()
if __name__=="__main__":
    main()