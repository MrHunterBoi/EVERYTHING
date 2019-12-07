import pygame
from ball import Ball
 
pygame.init()

width = int(input("Please enter max width: "))
height = int(input("Please enter max height: "))

BLACK = (0,0,0)
WHITE = (255,255,255)

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > height - height*0.13:
          self.rect.y = height - height*0.13

size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = width/100
paddleA.rect.y = height/2
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = width/100*99
paddleB.rect.y = height/2
 
ball = Ball(WHITE,10,10)
ball.rect.x = width/2
ball.rect.y = height/2

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

while carryOn:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     carryOn=False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)    

    all_sprites_list.update()

    if ball.rect.x>=width:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>height:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     
 
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
    
    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, [width/2, 0], [width/2, height], 5)

    all_sprites_list.draw(screen) 

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (width/3,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (width/3*2,10))

    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()