import math
class GasParticle:
	CONST_ATTRACTION = 0 # assuming it is a liquid with dipole dipole attractions
	CONST_REPULSION = 40
	PARTICLE_RADIUS = 1
	INFLUENCE_DISTANCE = 4
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


	def update_forces_from_particles(self, g = None):
		x = math.floor(self.xpos)
		y = math.floor(self.ypos)
		

		#edge cases for finding what range of particles are influential
		x_lower = x - GasParticle.INFLUENCE_DISTANCE
		if (x < GasParticle.INFLUENCE_DISTANCE):
			x_lower = 0

		y_lower = y - GasParticle.INFLUENCE_DISTANCE
		if (y < GasParticle.INFLUENCE_DISTANCE):
			y_lower = 0

		x_upper = x + GasParticle.INFLUENCE_DISTANCE
		if (x + GasParticle.INFLUENCE_DISTANCE > SIZE_SIMULATION_X):
			x_upper = SIZE_SIMULATION_X 

		y_upper = y + GasParticle.INFLUENCE_DISTANCE
		if (y + GasParticle.INFLUENCE_DISTANCE > SIZE_SIMULATION_Y):
			y_upper = SIZE_SIMULATION_Y


		particle_mat = [[g[x][y] for y in range(y, y_upper)] for x in range(x_lower, x_upper)] # particle matrix of influential particles stores in lists as cells
		
		for row in particle_mat:
			for col in row:
				for influential_particle in col:
					if (not influential_particle == p):
						# now we have a particle p that we can use
						difference_x = self.xpos - influential_particle.xpos
						difference_y = self.ypos - influential_particle.ypos
						distance = (difference_x**2 + difference_y**2)**0.5 # will be used for weighin calculations, simple pythag
						force_attraction = GasParticle.CONST_ATTRACTION*(1/distance)
						force_repulsion = -GasParticle.CONST_REPULSION*(1/(distance**0.5))
						
						x_dir = 1 # direction of x attraction and repulsion, negative to left and attraction to the right
						if (difference_x > 0):
							x_dir = -1

						y_dir = 1
						if (difference_y > 0):
							y_dir = -1
						# the lines above ensure that the forces are being applied in the right direction

						self.xvel = self.xvel + x_dir*(force_attraction + force_repulsion)*TIME_STEP
						self.yvel = self.yvel + x_dir*(force_attraction + force_repulsion)*TIME_STEP # force is an acceleration, and must be multiplied by dt to get change in velocity
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