import pygame
from random import randint

Black = (0,0,0)
class Ball(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		super().__init__()
		self.image = pygame.Surface([width,height])
		self.image.fill(Black)
		self.image.set_colorkey(Black)
		pygame.draw.rect(self.image,color,[0,0,width,height])
		self.velocity = [randint(4,8),randint(-4,8)]
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]
	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[0] = randint(-8,8)