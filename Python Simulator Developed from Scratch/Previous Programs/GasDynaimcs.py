class GasParticle:
	CONST_ATTRACTION = 0 # assuming it is a liquid with dipole dipole attractions
	CONST_REPULSION = 40
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