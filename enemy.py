from entity import *
from pygame.math import *
from collections import namedtuple
import bulletpattern

class Enemy(Entity):
	def __init__(self, rect, surf):
		Entity.__init__(self, rect, surf)
		#self.pattern = pattern.patternSquare(self)
		#self.pattern = pattern.Pattern3(self)
		self.bulletPattern = bulletpattern.Pattern1()

	def update(self, timePassed, target):
		self.timePassed+=timePassed
		self.updateMovementPattern()
		self.updateBulletPattern(target)
		self.updateRect()
		self.animation()
		self.timePassed = 0

	def updateMovementPattern(self):
		self.movementPattern.update(self.timePassed)
	
	def updateBulletPattern(self, target):
		self.bulletPattern.update(self, target, self.timePassed)


	def loadEnemy(self, pattern, name):
		self.movementPattern = pattern
		self.name = name

	#def setType(self, Type):
		#self.Type = Type

	def updateRect(self):
		Entity.updateRect(self)

