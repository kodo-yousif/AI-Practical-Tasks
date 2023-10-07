import os
import pygame

class Tiles:

	def __init__(self, number, xPos, yPos):
		self.number=number; 
		self.xPos = xPos; 
		self.yPos = yPos;

		assets_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)),"assets") 
		image_path = os.path.join(assets_path, f"{self.number}.png")
		

		self.image = pygame.image.load(image_path)



		self.image=pygame.transform.scale(self.image,(100,100))

		self.rectangle=self.image.get_rect()
			

	def im_vacuum(self): 
		self.number = 10
		assets_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)),"assets") 
		image_path = os.path.join(assets_path, "10.png")

		self.image =  pygame.image.load(image_path)
		self.image=pygame.transform.scale(self.image,(100,100))
		self.rectangle=self.image.get_rect()

	def im_floor(self): 
		self.number = 1
		assets_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)),"assets") 
		image_path = os.path.join(assets_path, "1.png")
		
		self.image =  pygame.image.load(image_path)
		self.image=pygame.transform.scale(self.image,(100,100))
		self.rectangle=self.image.get_rect()
		