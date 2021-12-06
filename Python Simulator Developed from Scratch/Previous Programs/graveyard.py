# This file is used for keeping track of old code that may be useful. 










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
REPUSION_SHIFT = 0.5

# obviously the attractions between molecules are more complex that what I will impliment
# however, this simplication allows for easy implimentation
# objects will be attracted via a force that has strength 1/(ax) with relation to the distance between them. 
# objects will be repulsed via a force that has strength 1/(bx)^2 with relation to the distance between them.
# where a << b
# the wall will act as a particle except it just repells the particle. 
# I know I am missusing force, however I will just add up the 'forces' of all of the 


PLOTTING_COLOR = 'black'

INFLUENCE_DISTANCE = 4

class GasParticle:
	CONST_ATTRACTION = 0 # assuming it is a gas with no attractions
	CONST_REPULSION = 40
	radius = 0.5
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
	def update_forces_from_particles(self, g):
		pass
	def change_velocities(p1, p2):
            """
            Particles p1 and p2 have collided elastically: update their
            velocities.

            """

            m1, m2 = p1.radius**2, p2.radius**2
            M = m1 + m2
            r1, r2 = p1.r, p2.r
            d = np.linalg.norm(r1 - r2)**2
            v1, v2 = p1.v, p2.v
            u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
            u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
            p1.v = u1
            p2.v = u2




class TeethParticles:
	CONST_ATTRACTION = 0 # for gasses or fixed points
	CONST_REPULSION = 40
	A = 5.4
	B = 7.7
	C = 0.8
	S = 12 # S for scaling the graph along the x axis
	# from graph here https://www.desmos.com/calculator/5ivqrz8tfl
	def __init__(self, xpos = 0, ypos = 0, xvel = 0, yvel = 0, radius = 1):
		self.xpos = xpos
		self.ypos = ypos
		self.xvel = xvel
		self.yvel = yvel
		self.radius = radius
	def update_forces_from_particles(self, s):

		pass
		# s is solid that it is interactin with 
class PawlParticles():
	CONST_ATTRACTION = 0 # for gasses or fixed points
	CONST_REPULSION = 40
	A = 5.4
	B = 7.7
	C = 0.8
	S = 12 # S for scaling the graph along the x axis
	# from graph here https://www.desmos.com/calculator/5ivqrz8tfl
	def __init__(self, xpos = 0, ypos = 0, xvel = 0, yvel = 0, radius = 1):
		self.xpos = xpos
		self.ypos = ypos
		self.xvel = xvel
		self.yvel = yvel
		self.radius = radius
	def update_forces_from_particles(self, g):

		pass


class FixedParticle:
	def __init__(self, xpos = 0, ypos = 0, xvel = 0, yvel = 0, radius = 1):
		self.xpos = xpos
		self.ypos = ypos
		self.xvel = xvel
		self.yvel = yvel
		self.radius = radius
	def update_forces_from_particles(self, g):
		
		pass
		# s is solid that it is interactin with 


def main(): 
# creates every particle with a random position
	newyet = TeethParticles()
	gas_particles = create_gas_particles()
	teeth_particles = create_teeth_particles()
	fixed_particles = create_fixed_particles()
	every_particle = gas_particles + teeth_particles + fixed_particles

	grid = [[list() for y in range (grid_y)] for x in range (grid_x)] 
	fill_grid(g = grid, ep = every_particle)

	current_time = 0
	
	while current_time < TOTAL_TIME:

		# run(every_particle, grid = grid)
		x_values = []
		y_values = []
		for p in every_particle:
			p.update_forces_from_particles(grid)
			# update_forces_from_particles(g = grid, p = p)
			update_forces_from_wall(p)
			update_position(in_particle = p, g = grid)
			x_values.append(p.xpos)
			y_values.append(p.ypos)
		plt.scatter(x_values, y_values, color = PLOTTING_COLOR, s = PARTICLE_RADIUS*100)
		# plt.quiver(p.xpos, p.ypos, p.xvel, p.yvel)
		plt.xlim(0, SIZE_SIMULATION_X)
		plt.ylim(0, SIZE_SIMULATION_Y)
		plt.show(block=False)
		plt.pause(TIME_STEP)
		plt.close()

		current_time = current_time + TIME_STEP
	# return()
	# print()
def create_gas_particles():
# i want to create every particle to be equally spaced initially as to avoid any close interations that shouldn't occur otherwise.
 # potential problen with this algorithim is that there can be some particle wall interactions that are undesirable initially (may overlap)
# desire is for particles to be equally spaced on one half of the simulation 
	return []
	# return [GasParticle(
	# 	xpos = (i) % (SIZE_SIMULATION_X/2), 
	# 	ypos = (i*(SIZE_SIMULATION_X**0.5)) % (SIZE_SIMULATION_X),
	# 	xvel = random.uniform(-1,1)*INITIAL_SPEED,
	# 	yvel = random.uniform(-1,1)*INITIAL_SPEED) 
	# for i in range (0, NUMBER_PARTICLES)]

def create_teeth_particles():
	a = []
	for x in range (0, 10):
		a = a + [TeethParticles(xpos = (8+x*0.1), ypos = (5+y*0.1)) for y in range(0, 10)]
	return a
def create_pawl_particles():
	return []
def create_fixed_particles():
	return []
	# return [FsixedParticle(xpos = 7, ypos = y*0.3) for y in range(0,33)]
	 # creates vertical wall

def get_influential_particles(g = None, p = None):
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


	return [[g[x][y] for y in range(y, y_upper)] for x in range(x_lower, x_upper)] # particle matrix of influential particles stores in lists as cells


def update_forces_from_particles(g = None, p = None):
	# old function, not used
	particle_mat = get_influential_particles(g = g, p = p)
	if (not type(p) == FixedParticle):

		for row in particle_mat:
			for col in row:
				for influential_particle in col:
					if (not influential_particle == p):
						difference_x = p.xpos - influential_particle.xpos
						difference_y = p.ypos - influential_particle.ypos
						distance = (difference_x**2 + difference_y**2)**0.5 # will be used for weighin calculations, simple pythag
						force_attraction = 0
						force_repulsion = 0
						if (not (type(p) == TeethParticles and type(influential_particle) == TeethParticles)):
							# now we have a particle p that we can use
							force_attraction = type(p).CONST_ATTRACTION*(1/distance)
							force_repulsion = -type(p).CONST_REPULSION*(1/(REPUSION_SHIFT+distance**2))
							

						else:
							force_attraction = TeethParticles.A/(TeethParticles.S*distance + TeethParticles.C) 
							force_repulsion = TeethParticles.B/((TeethParticles.S*distance)**2 + TeethParticles.C)
						x_dir = 1 # direction of x attraction and repulsion, negative to left and attraction to the right
						if (difference_x > 0):
							x_dir = -1

						y_dir = 1
						if (difference_y > 0):
							y_dir = -1
						# the lines above ensure that the forces are being applied in the right direction

						p.xvel = p.xvel + x_dir*(force_attraction + force_repulsion)*TIME_STEP
						p.yvel = p.yvel + x_dir*(force_attraction + force_repulsion)*TIME_STEP # force is an acceleration, and must be multiplied by dt to get change in velocity

							# dealing with Solid-Solid interactions


							# \frac{a}{\left(x+c\right)}-\frac{b}{x^{2}+c} equation govering solid solid interactions
							# created graph found here https://www.desmos.com/calculator/5ivqrz8tfl
	# elif (type(p) == TeethParticles):

	"""
				if (distance <= (radius + radius2)):
        xdistance = abs(center1.getX() - center2.getX())
        ydistance = abs(center1.getY() - center2.getY())

        if (xdistance <= ydistance):
            if ((self.vecti2 > 0 & bound1.y < bound3.y) | (self.vecti2 < 0 & bound1.y > bound3.y)):
                self.vecti2 = -self.vecti2


            if ((cir2.vecti2 > 0 & bound3.y < bound1.y) | (cir2.vecti2 < 0 & bound3.y > bound1.y)):
                cir2.vecti2 = -cir2.vecti2



        elif (xdistance > ydistance):
            if ((self.vecti1 > 0 & bound1.x < bound3.x) | (self.vecti1 < 0 & bound1.x > bound3.x)):
                self.vecti1 = -self.vecti1

            if ((cir2.vecti1 > 0 & bound3.x < bound1.x) | (cir2.vecti1 < 0 & bound3.x > bound1.x)):
                cir2.vecti1 = -cir2.vecti1

                code copied from https://stackoverflow.com/questions/32751130/python-2d-ball-collision



                m1, m2 = p1.radius**2, p2.radius**2
            M = m1 + m2
            r1, r2 = p1.r, p2.r
            d = np.linalg.norm(r1 - r2)**2
            v1, v2 = p1.v, p2.v
            u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
            u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
            p1.v = u1
            p2.v = u2
		more stolen code! from https://scipython.com/blog/two-dimensional-collisions/
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

def update_position(in_particle = None, g = None):
	# update grid here
	x = in_particle.xpos
	y = in_particle.ypos
	g[math.floor(x)][math.floor(y)].remove(in_particle)
	new_x = x + in_particle.xvel*TIME_STEP
	new_y = y + in_particle.yvel*TIME_STEP
	g[math.floor(new_x)][math.floor(new_y)].append(in_particle)
	in_particle.xpos = new_x
	in_particle.ypos = new_y

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






