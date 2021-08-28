import random
import math
import numpy as np

PARTICLE_RADIUS = 1
NUMBER_PARTICLES = 10
SIZE_SIMULATION_X = 100
SIZE_SIMULATION_Y = 100

INITIAL_SPEED = 10
TIME_STEP = 0.01
TOTAL_TIME = 10

grid_x = SIZE_SIMULATION_X
grid_y = SIZE_SIMULATION_Y

# obviously the attractions between molecules are more complex that what I will impliment
# however, this simplication allows for easy implimentation
# objects will be attracted via a force that has strength 1/(ax) with relation to the distance between them. 
# objects will be repulsed via a force that has strength 1/(bx)^2 with relation to the distance between them.
# where a << b
# the wall will act as a particle except it just repells the particle. 
# I know I am missusing force, however I will just add up the 'forces' of all of the 
CONST_ATTRACTION = 10 
CONST_REPULSION = 1
INFLUENCE_DISTANCE = 10

class Particle:
	def __init__ (self, xpos = 0, ypos = 0, xvec = 0, yvec = 0, radius = PARTICLE_RADIUS):
		# xpos and ypos show location of center of particle, 
		self.xpos = xpos
		self.ypos = ypos
		self.xvec = xvec
		self.yvec = yvec
		self.radius = radius
	def __str__ (self):
		return ("Center: " + "X coords: " + str(self.xpos) + " Y coords: " + str(self.ypos) +
			"\nX vector: " + str(self.xvec) + " Y vector: " + str(self.yvec) + 
			"\nRadius: " + str(self.radius))

def main(): 
# creates every particle with a random position
	every_particle = [Particle(
		xpos = random.uniform(PARTICLE_RADIUS, SIZE_SIMULATION_X - PARTICLE_RADIUS), 
		ypos = random.uniform(PARTICLE_RADIUS, SIZE_SIMULATION_Y - PARTICLE_RADIUS),
		xvec = random.uniform(-1,1)*INITIAL_SPEED,
		yvec = random.uniform(-1,1)*INITIAL_SPEED) 
	for i in range (0, NUMBER_PARTICLES)]

	grid = [[list() for y in range (grid_y)] for x in range (grid_x)] 
	fill_grid(g = grid, ep = every_particle)

	current_time = 0
	while current_time < TOTAL_TIME:
		run(every_particle)
		current_time = current_time + TIME_STEP

def run(ep = None):
	for p in ep:
		update_forces_from_particles(g = grid, p = p)
		update_forces_from_wall(p)
		update_position(p)


	# return()
	# print()

def update_forces_from_particles(g = None, p = None)
	x = math.floor(p.xpos)
	y = math.floor(p.ypos)
	
	y_lower = p.xpos
	if (p.xpos < INFLUENCE_DISTANCE):
		x_lower = 0

	if (p.xpos < INFLUENCE_DISTANCE):
		x_lower = 0

	influential_particles = list()




def update_forces_from_wall(in_particle):
	dist_x = in_particle.xvec*TIME_STEP

	xpos_updated = in_particle.xpos + in_particle.xvec*TIME_STEP
	if (xpos_updated < 0 or xpos_updated > SIZE_SIMULATION_X):
		in_particle.xvec = in_particle.xvec*(-1)

	ypos_updated = in_particle.ypos + in_particle.yvec*TIME_STEP
	if (ypos_updated < 0 or ypos_updated > SIZE_SIMULATION_Y):
		in_particle.yvec = in_particle.yvec*(-1)
	pass

def update_position(in_particle):
	in_particle.xpos = in_particle.xpos + in_particle.xvec*TIME_STEP
	in_particle.ypos = in_particle.ypos + in_particle.yvec*TIME_STEP
	pass

def fill_grid(g = None, ep = None):
	for p in ep:

		x = math.floor(p.xpos)
		y = math.floor(p.ypos)
		g[x][y].append(p)
	pass



main()






