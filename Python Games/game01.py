import random
import math
# pyglet
from euclid import Vector2
from pygame.locals import QUIT
import pygame

#Constants
colors = []
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
FPS_LIMIT = 60
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (218, 165, 65)

class Circle(object):
	"""docstring for Circle"""
	def __init__(self, position, velocity, radius, color, width = random.randint(1,4)):
		self.position = position
		self.velocity = velocity
		self.radius = radius
		self.color = color
		self.width = width
	def _bounce(self):
		left_margin = self.radius
		right_margin = SCREEN_WIDTH - self.radius
		top_margin = self.radius
		bottom_margin = SCREEN_HEIGHT - self.radius

		if self.position.x <= left_margin:
			self.position.x = 2 * left_margin - self.position.x
			self.velocity = self.velocity.reflect(Vector2(1,0))
		elif self.position.x >= right_margin:
			self.position.x = 2 * right_margin - self.position.x
			self.velocity = self.velocity.reflect(Vector2(1,0))

		if self.position.y <= top_margin:
			self.position.y = 2 * top_margin - self.position.y
			self.velocity = self.velocity.reflect(Vector2(0,1))
		elif self.position.y >= bottom_margin:
			self.position.y = 2 * bottom_margin - self.position.y
			self.velocity = self.velocity.reflect(Vector2(0,1))
	def _get_next_position(self,dt):
		return self.position + 0.5 * self.accel * dt**2 - self.elocity * dt

	def draw(self, surface):
		pos = (int (self.position.x),int (self.position.y))
		pygame.draw.circle(
			surface,
			self.color,
			pos,
			self.radius,
			self.width
		)
	def collide(self, other):
		collision_vector = (self.position - other.position).normalize()
		self.velocity = self.velocity.reflect(collision_vector)
		other.velocity = other.velocity.reflect(collision_vector)
	
	def surface_distance(self,other, dt):
		#Equation for distance between surfaces
		# d(t) = || pos1(t) - pos2(t)|| - (r1 + r2)
		pos1 = self._get_next_position(dt)
		pos2 = other._get_next_position(dt)
		return abs(pos1 - pos2) - (self.radius + other.radius)

	def move(self, dt):
		self.position = self._get_next_position(dt)
		self._bounce()
def A ():
		return (random.randint(1,255),random.randint(50,150),random.randint(2,255))

def add_color(numbers):
	for a in range(numbers):
		colors.append(A())
def rand():
	return random.randint(10,20)
def get_random_velocity(speed):
	angle = random.uniform(0, 2*math.pi)
	x = math.cos(angle)
	y = math.sin(angle)
	init_vector = Vector2(x,y)
	return speed * init_vector

def main():
	speed = 70 #pixels per second
	number_of_circles = 150
	add_color(number_of_circles)
	gravity = Vector2(0, 20) #pixel per seconds per seconds
	#initialize the display the windows
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	circles = []
	for i in range(number_of_circles):
		radius = rand()
		x = random.randint(radius, SCREEN_WIDTH - radius)
		y = random.randint(radius, SCREEN_HEIGHT - radius)
		position = Vector2(x,y)
		velocity = get_random_velocity(speed)
		color = random.choice(colors)
		circles.append( Circle(position, velocity, gravity, radius, color))
	### GAME LOOP###

	clock = pygame.time.Clock()
	running = True

	while running:

		#break out of game loop if the window is closed
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
		# get the time elpasef
		dt_ms = clock.tick(FPS_LIMIT) #miliseconds
		dt = dt_ms / 1000 # convert to seconds

		# make the background is white
		screen.fill(GOLD)

		#move the circles and draw them
		for i, circle in enumerate(circles):
			circle.move(dt)
			for other_circle in circles[i+1:]:
				if circle.surface_distance(other_circle,dt) <= 0:
					circle.collide(other_circle)

		for circle in circles:
			circle.move(dt)
			circle.draw(screen)

		pygame.display.flip()

pygame.quit()



if __name__ == '__main__':
	main()