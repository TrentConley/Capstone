class SolidParticle():
	CONST_ATTRACTION = 100 # assuming it is a liquid with dipole dipole attractions
	CONST_REPULSION = 40
	def __init__(self, xpos = 0, ypos = 0, xvel = 0, yvel = 0, radius = 1):
		self.xpos = xpos
		self.ypos = ypos
		self.xvel = xvel
		self.yvel = yvel
		self.radius = radius
	def calculate_interactions_solid(self, s):

		# s is solid that it is interactin with 