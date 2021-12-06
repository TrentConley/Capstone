import random
import math
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# particle simulator: https://www.youtube.com/watch?v=HWSKS2rD44g

PARTICLE_RADIUS = 1
NUMBER_PARTICLES = 20
SIZE_SIMULATION_X = 10
SIZE_SIMULATION_Y = 10

INITIAL_SPEED = 10
TIME_STEP = 0.01
TOTAL_TIME = 1

grid_x = SIZE_SIMULATION_X
grid_y = SIZE_SIMULATION_Y

# obviously the attractions between molecules are more complex that what I will impliment
# however, this simplication allows for easy implimentation
# objects will be attracted via a force that has strength 1/(ax) with relation to the distance between them. 
# objects will be repulsed via a force that has strength 1/(bx)^2 with relation to the distance between them.
# where a << b
# the wall will act as a particle except it just repells the particle. 
# I know I am missusing force, however I will just add up the 'forces' of all of the 
CONST_ATTRACTION = 0 # assuming it is a liquid with dipole dipole attractions
CONST_REPULSION = 40
PLOTTING_COLOR = 'black'

INFLUENCE_DISTANCE = 4

class Particle:
	def __init__ (self, xpos = 0, ypos = 0, xvel = 0, yvel = 0, radius = PARTICLE_RADIUS):
		# xpos and ypos show location of center of particle, 
		self.xpos = xpos
		self.ypos = ypos
		self.xvel = xvel
		self.yvel = yvel
		self.radius = radius
	def __str__ (self):
		return ("Center: " + "X coords: " + str(self.xpos) + " Y coords: " + str(self.ypos) +
			"\nX vector: " + str(self.xvel) + " Y vector: " + str(self.yvel) + 
			"\nRadius: " + str(self.radius))

class Solid_Particle():
	
	def __init__(self, xpos = 0, ypos = 0, xvel = 0, yvel = 0, radius = PARTICLE_RADIUS):
		self.xpos = xpos
		self.ypos = ypos
		self.xvel = xvel
		self.yvel = yvel
		self.radius = radius


def main(): 
# creates every particle with a random position
	every_particle = create_gas_particles()

	grid = [[list() for y in range (grid_y)] for x in range (grid_x)] 
	fill_grid(g = grid, ep = every_particle)

	current_time = 0
	
	while current_time < TOTAL_TIME:

		# run(every_particle, grid = grid)
		for p in every_particle:
			update_forces_from_particles(g = grid, p = p)
			update_forces_from_wall(p)
			update_position(p)
			
			plt.scatter(p.xpos, p.ypos, color = PLOTTING_COLOR)
		# plt.quiver(p.xpos, p.ypos, p.xvel, p.yvel)
		plt.xlim(0, SIZE_SIMULATION_X)
		plt.ylim(0, SIZE_SIMULATION_Y)
		plt.show(block=False)
		plt.pause(0.0001/TIME_STEP)
		plt.close()



		current_time = current_time + TIME_STEP
	# return()
	# print()
def create_gas_particles():

	return [Particle(
		xpos = random.uniform(PARTICLE_RADIUS, SIZE_SIMULATION_X - PARTICLE_RADIUS), 
		ypos = random.uniform(PARTICLE_RADIUS, SIZE_SIMULATION_Y - PARTICLE_RADIUS),
		xvel = random.uniform(-1,1)*INITIAL_SPEED,
		yvel = random.uniform(-1,1)*INITIAL_SPEED) 
	for i in range (0, NUMBER_PARTICLES)]


def update_forces_from_particles(g = None, p = None):
	x = math.floor(p.xpos)
	y = math.floor(p.ypos)
	

	#edge cases for finding what range of particles are influential
	x_lower = x - INFLUENCE_DISTANCE
	if (x < INFLUENCE_DISTANCE):
		x_lower = 0

	y_lower = y - INFLUENCE_DISTANCE
	if (y < INFLUENCE_DISTANCE):
		y_lower = 0

	x_upper = x + INFLUENCE_DISTANCE
	if (x + INFLUENCE_DISTANCE > SIZE_SIMULATION_X):
		x_upper = SIZE_SIMULATION_X 

	y_upper = y + INFLUENCE_DISTANCE
	if (y + INFLUENCE_DISTANCE > SIZE_SIMULATION_Y):
		y_upper = SIZE_SIMULATION_Y


	particle_mat = [[g[x][y] for y in range(y, y_upper)] for x in range(x_lower, x_upper)] # particle matrix of influential particles stores in lists as cells
	
	for row in particle_mat:
		for col in row:
			for influential_particle in col:
				if (not influential_particle == p):
					# now we have a particle p that we can use
					difference_x = p.xpos - influential_particle.xpos
					difference_y = p.ypos - influential_particle.ypos
					distance = (difference_x**2 + difference_y**2)**0.5 # will be used for weighin calculations, simple pythag
					force_attraction = CONST_ATTRACTION*(1/distance)
					force_repulsion = -CONST_REPULSION*(1/(distance**0.5))
					
					x_dir = 1 # direction of x attraction and repulsion, negative to left and attraction to the right
					if (difference_x > 1):
						x_dir = -1

					y_dir = 1
					if (difference_y > 1):
						y_dir = -1
					# the lines above ensure that the forces are being applied in the right direction

					p.xvel = p.xvel + x_dir*(force_attraction + force_repulsion)*TIME_STEP
					p.yvel = p.yvel + x_dir*(force_attraction + force_repulsion)*TIME_STEP # force is an acceleration, and must be multiplied by dt to get change in velocity
	"""
				// get the mtd
			    Vector2d delta = (position.subtract(ball.position));
			    float d = delta.getLength();
			    // minimum translation distance to push balls apart after intersecting
			    Vector2d mtd = delta.multiply(((getRadius() + ball.getRadius())-d)/d); 


			    // resolve intersection --
			    // inverse mass quantities
			    float im1 = 1 / getMass(); 
			    float im2 = 1 / ball.getMass();

			    // push-pull them apart based off their mass
			    position = position.add(mtd.multiply(im1 / (im1 + im2)));
			    ball.position = ball.position.subtract(mtd.multiply(im2 / (im1 + im2)));

			    // impact speed
			    Vector2d v = (this.velocity.subtract(ball.velocity));
			    float vn = v.dot(mtd.normalize());

			    // sphere intersecting but moving away from each other already
			    if (vn > 0.0f) return;

			    // collision impulse
			    float i = (-(1.0f + Constants.restitution) * vn) / (im1 + im2);
			    Vector2d impulse = mtd.normalize().multiply(i);

			    // change in momentum
			    this.velocity = this.velocity.add(impulse.multiply(im1));
			    ball.velocity = ball.velocity.subtract(impulse.multiply(im2));
"""

	# for row in particle_mat:
	# 	for col in p:
	# 		for l in col:
	# 			for p in l:
	# 				print(p)
def print_mat(mat):
	for x in mat:
		# print()
		# print (x)
		for y in x:
			# print()
			# print(y)
			for p in y:
				print(p)
				# ok so where i am at, i have successfully gotten each particle to print in the close matrix

def update_forces_from_wall(in_particle):
	dist_x = in_particle.xvel*TIME_STEP

	xpos_updated = in_particle.xpos + in_particle.xvel*TIME_STEP
	if (xpos_updated < 0 or xpos_updated > SIZE_SIMULATION_X):
		in_particle.xvel = in_particle.xvel*(-1)

	ypos_updated = in_particle.ypos + in_particle.yvel*TIME_STEP
	if (ypos_updated < 0 or ypos_updated > SIZE_SIMULATION_Y):
		in_particle.yvel = in_particle.yvel*(-1)
	pass

def update_position(in_particle):
	in_particle.xpos = in_particle.xpos + in_particle.xvel*TIME_STEP
	in_particle.ypos = in_particle.ypos + in_particle.yvel*TIME_STEP
	pass

def fill_grid(g = None, ep = None):
	for p in ep:
		x = math.floor(p.xpos)
		y = math.floor(p.ypos)
		g[x][y].append(p)
	pass

def print_every_particle(ep):
	for p in ep:
		print (p)

	
main()






