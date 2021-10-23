import random
import math
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



# particle simulator: https://www.youtube.com/watch?v=HWSKS2rD44g

PARTICLE_RADIUS = 0.5
NUMBER_PARTICLES = 20
SIZE_SIMULATION_X = 100
SIZE_SIMULATION_Y = 100

INITIAL_SPEED = 10
TIME_STEP = 0.01
TOTAL_TIME = 1000
# need to include grid partitions so that it can be more precise than just 1. 
grid_x = SIZE_SIMULATION_X
grid_y = SIZE_SIMULATION_Y
REPUSION_SHIFT = 0.5
SOLID_SPACING = 1.5

# obviously the attractions between molecules are more complex that what I will impliment
# however, this simplication allows for easy implimentation
# objects will be attracted via a force that has strength 1/(ax) with relation to the distance between them. 
# objects will be repulsed via a force that has strength 1/(bx)^2 with relation to the distance between them.
# where a << b
# the wall will act as a particle except it just repells the particle. 
# I know I am missusing force, however I will just add up the 'forces' of all of the 


PLOTTING_COLOR = 'black'

INFLUENCE_DISTANCE = math.ceil(PARTICLE_RADIUS*2.1) # 2.1 because it is slightly larger than the max collision distance for particles

class GasParticle:


	def __init__ (self, xpos = 0, ypos = 0, xvel = 0, yvel = 0, radius = PARTICLE_RADIUS):
		# xpos and ypos show location of center of particle, 
		self.pos = np.array((xpos, ypos))
		self.v = np.array((xvel, yvel))
		self.radius = radius

	def __str__ (self):
		return ("Center: " + "X coords: " + str(self.xpos) + " Y coords: " + str(self.ypos) +
			"\nX vector: " + str(self.xvel) + " Y vector: " + str(self.yvel) + 
			"\nRadius: " + str(self.radius))

	# def change_velocities(self, p2):
 #            """
 #            Particles self and p2 have collided elastically: update their
 #            velocities.
 #            """
 #            m1, m2 = self.radius**2, p2.radius**2
 #            M = m1 + m2
 #            r1, r2 = self.r, p2.r
 #            d = np.linalg.norm(r1 - r2)**2
 #            v1, v2 = self.v, p2.v
 #            u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
 #            u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
 #            self.v = u1
 #            self.xvel = self.v[0]
 #            self.yvel = self.v[1]
 #            p2.v = u2
 #            p2.xvel = p2.v[0]
 #            p2.yvel = p2.v[1]

	def update_forces_from_particles(self, g):
		particle_mat = self.get_influential_particles(g)
		if (not type(self) == FixedParticle):

			for row in particle_mat:
				for col in row:
					for influential_particle in col:
						if ((not influential_particle == self) and type(influential_particle) == GasParticle):
							difference_x = self.pos[0] - influential_particle.pos[0]
							difference_y = self.pos[1] - influential_particle.pos[1]
							distance = (difference_x**2 + difference_y**2)**0.5 # willbe used for weighin calculations, simple pythag
							if (distance < self.radius + influential_particle.radius):
								elastic_collision(self, influential_particle)
								# self.change_velocities(influential_particle)
							# force_attraction = 0

							# force_repulsion = 0
							# if (not (type(self) == TeethParticle and type(influential_particle) == TeethParticle)):
							# 	# now we have a particle p that we can use
							# 	force_attraction = type(self).CONST_ATTRACTION*(1/distance)
							# 	force_repulsion = -type(self).CONST_REPULSION*(1/(REPUSION_SHIFT+distance**2))
								

							# else:
							# 	force_attraction = TeethParticle.A/(TeethParticle.S*distance + TeethParticle.C) 
							# 	force_repulsion = TeethParticle.B/((TeethParticle.S*distance)**2 + TeethParticle.C)
							# x_dir = 1 # direction of x attraction and repulsion, negative to left and attraction to the right
							# if (difference_x > 0):
							# 	x_dir = -1

							# y_dir = 1
							# if (difference_y > 0):
							# 	y_dir = -1
							# # the lines above ensure that the forces are being applied in the right direction

							# self.xvel = self.xvel + x_dir*(force_attraction + force_repulsion)*TIME_STEP
							# self.yvel = self.yvel + x_dir*(force_attraction + force_repulsion)*TIME_STEP # force is an acceleration, and must be multiplied by dt to get change in velocity

	def get_influential_particles(self, g):
		x = math.floor(self.pos[0])
		y = math.floor(self.pos[1])
		

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


class TeethParticle:
	SPRING_REST_DISTANCE = 1.5
	K_SPRING = 10
	A = 1.5 #reflects nature of ionic compounds; 
	B = 1
	C = 12 # coeffiecint on natural log term 
	S = 1/SOLID_SPACING # for scaling along x axis
	# from graph here https://www.desmos.com/calculator/5ivqrz8tfl
	def __init__(self, xpos = 0, ypos = 0, xvel = 0, yvel = 0, radius = PARTICLE_RADIUS, neighbors = []):
		self.pos = np.array((xpos, ypos))
		self.v = np.array((xvel, yvel))
		self.radius = radius
		self.neighbors = neighbors
	def update_forces_from_particles(self, g):

		# if len(self.neighbors) > 4:
		for p in self.neighbors:
			# for some reason the program thinks that the neighbors are beyond the stretch distance right now.
			# forces acting upon each particle from neighbors, acting like spring. 
			difference_x = self.pos[0] - p.pos[0]
			difference_y = self.pos[1] - p.pos[1]
			if (difference_x == 0):
				if (difference_y > 0):
					theta = math.pi/2
				else:
					theta = -math.pi/2
			else:
				theta = np.arctan(difference_y/difference_x) # gives angle between points

			distance = math.sqrt((difference_x**2 + difference_y**2))	
			if (distance < self.radius + p.radius):
				elastic_collision(self, p)
				print("not supposed to happen")

			else:

				# use equation for elastic collisions in combo with interaction equation
				# from https://www.desmos.com/calculator/mn3yfk4pgh
			# y=\frac{B}{sx}-\frac{A}{\left(sx\right)^{2}}-\frac{1}{4}\ln\left(sx\right)\left\{x\ >0\right\}
			# there will be too much repulsion and attraction on the tails if I don't include the ln term. 
				# attraction = (TeethParticle.B/(TeethParticle.S*distance) - TeethParticle.A/((TeethParticle.S*distance)**2) - (TeethParticle.C)*np.log(TeethParticle.S*distance))*TIME_STEP #with log
				# attraction = (TeethParticle.B/(TeethParticle.S*distance) - TeethParticle.A/((TeethParticle.S*distance)**2))*TIME_STEP #not log
				attraction = (distance - TeethParticle.SPRING_REST_DISTANCE)*TeethParticle.K_SPRING*TIME_STEP
				self.v[0] += np.cos(theta)*attraction
				self.v[1] += np.sin(theta)*attraction
				p.v[0] += np.cos(math.pi + theta)*attraction
				p.v[1] += np.sin(math.pi + theta)*attraction

					# change the velocites as per Hooke's Law
				# calculate the spring interactions between particles

		particle_mat = get_influential_particles(p =self, g = g, d = 2*self.radius)
		if (not type(self) == FixedParticle):

			for row in particle_mat:
				for col in row:
					for influential_particle in col:
						# teeth particles will still elastically collide. 
						if ((not influential_particle == self)):
							difference_x = self.pos[0] - influential_particle.pos[0]
							difference_y = self.pos[1] - influential_particle.pos[1]
							distance = math.sqrt((difference_x**2 + difference_y**2)) 
							print(distance)
							if (distance < self.radius + influential_particle.radius):
								print("collision!")
								elastic_collision(self, influential_particle)
								# why are the teeth coming closer after every run? shouldnt they also be equidistanct upon initialization?


		# treat interactinos among teeth particles, treat all else like elastic collisions. 0


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
			x_values.append(p.pos[0])
			y_values.append(p.pos[1])
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
	# return []
	return [GasParticle(
		xpos = (i) % (SIZE_SIMULATION_X/2), 
		ypos = (i*(SIZE_SIMULATION_X**0.5)) % (SIZE_SIMULATION_X),
		xvel = random.uniform(-1,1)*INITIAL_SPEED,
		yvel = random.uniform(-1,1)*INITIAL_SPEED) 
	for i in range (0, NUMBER_PARTICLES)]

# xpart, ypart are partitions for how many particles per span in x or y direction
def create_teeth_particles(xstart = 50, ystart = 50, xnumber = 10, ynumber = 10, yspan = 20):
	a = [None] * xnumber
	for x in range (0, xnumber):
		buildarr = [] #this is a funky way to create all of the particles
		xpos = x*SOLID_SPACING + xstart			
		for y in range (0, ynumber):

			ypos = y*SOLID_SPACING + ystart
			buildarr.append(TeethParticle(xpos = xpos, ypos = ypos))
		a[x] = buildarr
	i = 0
	# print (len(a))
	# print_mat(a)
	for x in range (0, xnumber):
		for y in range(0, ynumber):
			if (not x == 0):
							# 	print (i)
			# 	i = i+1
				# print (str(a[x][y]) + "this is one")
				a[x][y].neighbors = a[x][y].neighbors + [a[x-1][y]]
				print()
			if (not x == xnumber -1):
				# a[x][y].neighbors.append(a[x+1][y])
				a[x][y].neighbors = a[x][y].neighbors + [a[x+1][y]]
			if not (y == 0):
				# a[x][y].neighbors.append(a[x][y-1])
				a[x][y].neighbors = a[x][y].neighbors + [a[x][y-1]]
			if not (y == ynumber - 1):
				# a[x][y].neighbors.append(a[x][y+1])
				a[x][y].neighbors = a[x][y].neighbors + [a[x][y+1]]
			print ('\n')
			print(a[x][y].pos)
			print ('\n')
			[print (x.pos) for x in a[x][y].neighbors]

	aa = []
	for x in a:
		aa.extend(x)
	# print_mat(aa)
	return aa
	# return [TeethParticle(xpos = 8, ypos = 5+y*0.1) for y in range(0, 10)]
def create_pawl_particles():
	return []
def create_fixed_particles():
	return []
	# return [FsixedParticle(xpos = 7, ypos = y*0.3) for y in range(0,33)]
	 # creates vertical wall

def get_influential_particles(g = [[]], p = None, d = INFLUENCE_DISTANCE):
	x = math.floor(p.pos[0])
	y = math.floor(p.pos[1])
	

	#edge cases for finding what range of particles are influential
	x_lower = int(x - d)
	if (x < d):
		x_lower = 0

	y_lower = int(y - d)
	if (y < d):
		y_lower = 0

	x_upper = int(x + d)
	if (x + d > SIZE_SIMULATION_X):
		x_upper = SIZE_SIMULATION_X 

	y_upper = int(y + d)
	if (y + d > SIZE_SIMULATION_Y):
		y_upper = SIZE_SIMULATION_Y
	return [[g[x][y] for y in range(y_lower, y_upper)] for x in range(x_lower, x_upper)] # particle matrix of influential particles stores in lists as cells



def print_mat(mat):
	for x in mat:
		# print()
		
		for y in x:
			print (str(y.pos[0]) + " " + str(y.pos[1]))
			# print()
			# print(y)
			# for p in y:
			# 	print(p)
				# ok so where i am at, i have successfully gotten each particle to print in the close matrix

def update_forces_from_wall(in_particle):

	xpos_updated = in_particle.pos[0] + in_particle.v[0]*TIME_STEP
	if (xpos_updated < 0 or xpos_updated > SIZE_SIMULATION_X):
		in_particle.v[0] = in_particle.v[0]*(-1)

	ypos_updated = in_particle.pos[1] + in_particle.v[1]*TIME_STEP
	if (ypos_updated < 0 or ypos_updated > SIZE_SIMULATION_Y):
		in_particle.v[1] = in_particle.v[1]*(-1)

	pass

def update_position(in_particle = None, g = None):
	# update grid here
	x = in_particle.pos[0]
	y = in_particle.pos[1]
	g[math.floor(x)][math.floor(y)].remove(in_particle)

	new_x = x + in_particle.v[0]*TIME_STEP
	new_y = y + in_particle.v[1]*TIME_STEP
	try:
		g[math.floor(new_x)][math.floor(new_y)].append(in_particle)
	except IndexError:
		print("x: " + str(math.floor(new_x)))
		print("y: " + str(math.floor(new_y)))
		print(g[new_x][new_y])
	in_particle.pos = np.array((new_x, new_y))

	pass

def fill_grid(g = None, ep = None):
	for p in ep:
		x = math.floor(p.pos[0])
		y = math.floor(p.pos[1])
		g[x][y].append(p)
	pass

def print_every_particle(ep):
	for p in ep:
		print (p)

def elastic_collision(p1, p2):
	if (type(p1) == TeethParticle and type(p2) == TeethParticle):
		print ("teeth on teeth collision")
	"""
    Particles self and p2 have collided elastically: update their
    velocities.
    """
	m1, m2 = p1.radius**2, p2.radius**2
	M = m1 + m2
	r1, r2 = p1.pos, p2.pos
	d = np.linalg.norm(r1 - r2)**2
	v1, v2 = p1.v, p2.v
	u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
	u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
	p1.v = u1

	p2.v = u2



	
main()


