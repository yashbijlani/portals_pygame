import pygame

pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width,height))
color = (0, 0, 0)
objectColor = (200, 200, 200)
window.fill(color)
pygame.display.flip()

run = True

class Character:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.image = pygame.image.load("//home//kaliv1//Pictures//blob.gif").convert()
		self.image = pygame.transform.scale(self.image, (150, 75))
		self.speed = 5  
		self.teleporting = False
		self.canTeleport = True
		self.cooldown = pygame.USEREVENT + 0
		pygame.time.set_timer(self.cooldown, 2000)
	def move(self, direction):
		if direction == 'w':
			self.y -= self.speed
		elif direction == 's':
			self.y += self.speed
		elif direction == 'a':
			self.x -= self.speed
		elif direction == 'd':
			self.x += self.speed

	def display(self, window):
		window.blit(self.image, (self.x, self.y))
	def redisplay(self, xx, yy):
		window.blit(self.image, (xx, yy))
    	
class Portal():
	def __init__(self,x,y):
		self.x = x
		self.y = y 
		self.delx = 150
		self.dely = 75
		self.portalimg = pygame.image.load("//home//kaliv1//Pictures//portal.png").convert()
		self.portalimg = pygame.transform.scale(self.portalimg, (self.delx, self.dely))
		self.portalimg = pygame.transform.rotate(self.portalimg, 90)
	def display(self):
		window.blit(self.portalimg, (self.x, self.y))
	def colCheck(self, xx, yy, character, portal2):
		character_rect = pygame.Rect(character.x, character.y, character.image.get_width(), character.image.get_height())
		portal_rect = pygame.Rect(self.x, self.y, self.delx, self.dely)
		if character_rect.colliderect(portal_rect) and character.teleporting==True:
			character.teleporting = False
		elif character.canTeleport==True and character_rect.colliderect(portal_rect) and character.teleporting==False:
			character.x = portal2.x
			character.y = portal2.y
			character.teleporting = True
			character.canTeleport = False

			
p1 = Portal(100, 100)
p2 = Portal(600, 300)
character = Character(400, 300)

while run:
	clock = pygame.time.Clock()
	clock.tick(60)
	for event in pygame.event.get():
		if event.type  == pygame.QUIT:
			run = False
		if event.type == character.cooldown:
			character.canTeleport = True
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		character.move('w')
	if keys[pygame.K_s]:
		character.move('s')
	if keys[pygame.K_a]:
		character.move('a')
	if keys[pygame.K_d]:
		character.move('d')

	window.fill((0, 0, 0))  
	p1.display()
	p2.display()
	character.display(window)
	p1.colCheck(character.x, character.y, character, p2)
	p2.colCheck(character.x, character.y, character, p1)
	pygame.display.flip()
pygame.QUIT()
