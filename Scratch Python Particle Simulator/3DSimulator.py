# axes = [0, 2, 1] first two are the planes we are graphing in, last one we are not





# 3D simulation of bouncing particles
#
# author: Konstantin Lübeck (Embedded Systems, Universtiy of Tuebingen)
# adapted from: Stephan Schirrecker (schirrecker) 
# https://gist.github.com/schirrecker/982847faeea703dd6f1dd8a09eab13aa
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# gravitational acceleration on Earth in m*s^-2
# g = 9.80665
g = 0

# acceleration vector due to g
ag = np.array((0, 0, -g))

# coefficient of restitution (ratio of velocity after and before bounce)
# see http://en.wikipedia.org/wiki/Coefficient_of_restitution
cor = 1.0

# 1 millisecond delta t
delta_t = 0.001

# number of particles to simulate
num_particles = 10

# size of the x, y, and z axis
size = 10

# colors of the particles
colors = ['b', 'g', 'r', 'c', 'm', 'y']

# inital view angles
# elev = 30
elev = 0
# azim = 30
azim = 90

xlim = (0,size)
ylim = (0,size)
zlim = (0,size)

# number of partitions in grid to zoom in on particle dynamics
grid_partition = 1

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_zlim(zlim)

ax.view_init(elev, azim)
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')

particles = [] # need to to set up as global
grid = [] # need to set up as global 
class particle:
    def __init__(self, xyz, v, fmt, radius = 0.1):
        self.xyz = np.array(xyz)
        self.v = np.array(v)
        self.radius = radius

        self.scatter, = ax.plot([], [], [], fmt, animated=True)

    def does_elastic_collision_occur(self):
        # here we will first check if there will be an elastic collision.
        # first we need to get all of the potential collisions from the grid. 


        return [False, None]

    def deal_with_elastic_collision(self, b):
        return []

    def update(self, grid):
        # particle hits lower x wall 
        # if self.xyz[0] <= xlim[0]:
        #     self.v[0] = cor * np.abs(self.v[0])

        # # particle hits upper x wall
        # elif self.xyz[0] >= xlim[1]:
        #     self.v[0] = - cor * np.abs(self.v[0])

        # # particle hits lower y wall
        # if self.xyz[1] <= ylim[0]:
        #     self.v[1] = cor * np.abs(self.v[1])

        # # particle hits upper y wall
        # elif self.xyz[1] >= ylim[1]:
        #     self.v[1] = - cor * np.abs(self.v[1])

        # # particle hits lower z wall
        # if self.xyz[2] <= zlim[0]:
        #     self.v[2] = cor * np.abs(self.v[2])

        # # particle hits upper z wall
        # elif self.xyz[2] >= zlim[1]:
        #     self.v[2] = - cor * np.abs(self.v[2])
        update_forces_from_wall(self)
        # changing velocity due to acceleration of gravity
        delta_v = delta_t * ag
        self.v += delta_v
        collision_info = self.does_elastic_collision_occur()
        if (collision_info[0]):
            self.deal_with_elastic_collision(collision_info[1])
        update_position(in_particle = self, g = grid)


        # make sure the particles stay inside of the canvas
        self.xyz[0] = np.clip(self.xyz[0], xlim[0], xlim[1])
        self.xyz[1] = np.clip(self.xyz[1], ylim[0], ylim[1])
        self.xyz[2] = np.clip(self.xyz[2], zlim[0], zlim[1])

        # draw particle
        self.scatter.set_xdata(self.xyz[0])
        self.scatter.set_ydata(self.xyz[1])
        self.scatter.set_3d_properties(self.xyz[2])


def update_forces_from_wall(in_particle):

    xpos_updated = in_particle.xyz[0] + in_particle.v[0]
    if (xpos_updated < xlim[0] or xpos_updated > xlim[1]):
        in_particle.v[0] = in_particle.v[0]*(-1)

    ypos_updated = in_particle.xyz[1] + in_particle.v[1]
    if (ypos_updated < ylim[0] or ypos_updated > ylim[1]):
        in_particle.v[1] = in_particle.v[1]*(-1)

    zpos_updated = in_particle.xyz[2] + in_particle.v[2]
    if (zpos_updated < zlim[0] or zpos_updated > zlim[1]):
        in_particle.v[2] = in_particle.v[2]*(-1)

    pass

def update_position(in_particle = None, g = None):
    # update grid here
    x, y, z = in_particle.xyz[0], in_particle.xyz[1], in_particle.xyz[2]
    new_x, new_y, new_z = x + in_particle.v[0], y + in_particle.v[1], z + in_particle.v[2]
    x_floor, y_floor, z_floor, new_x_floor, new_y_floor, new_z_floor = (math.floor(x), math.floor(y), 
        math.floor(z), math.floor(new_x), math.floor(new_y), math.floor(new_z))

    # working with x-z plane
    if (not (in_particle in g[new_x_floor][new_z_floor])):
        g[math.floor(x)][math.floor(z)].remove(in_particle)

    
    # try:
        g[math.floor(new_x)][math.floor(new_z)].append(in_particle)

        
    # except IndexError:
    #     print("x: " + str(math.floor(new_x)))
    #     print("y: " + str(math.floor(new_y)))
    #     print(g[new_x][new_y])
    in_particle.xyz[0] = new_x
    in_particle.xyz[1] = new_y
    in_particle.xyz[2] = new_z

    pass  
        
def fill_grid(g = None, ep = None):
    # again, also in the x-z plane
    for p in ep:
        x = math.floor(p.xyz[0])
        z = math.floor(p.xyz[2])
        g[x][z].append(p)
    pass

def init():
    return [] 

def update(t):

    global elev, azim

    for particle in particles:
        particle.update(grid)

    artists = [particle.scatter for particle in particles]
  
    # rotate view
    # azim = azim + t/2
    # ax.view_init(elev, azim)
    
    artists.append(ax)

    return artists

    # generate particles with random position, velocity, and color

for i in np.arange(0,num_particles):
    xyz = np.random.rand(1,3)[0]*size
    xyz[1] = 5 # for 2 dimensional dynamics
    v = np.random.rand(1,3)[0]*0.1
    # v[1] = 0 # for 2 dimensional dynamics
    # v[2] = 1
    # there will only be x-z dynamics.
    fmt = str(colors[np.random.randint(0,len(colors))] + 'o')
    particles.append(particle(xyz, v, fmt))

grid = [[list() for y in range (ylim[0], ylim[1])] for x in range (xlim[0], xlim[1])] # for efficient computation
fill_grid(g = grid, ep = particles)

ani = FuncAnimation(fig, update, frames=np.arange(0,0.5,delta_t), init_func=init, interval=10, blit=True, repeat=True)
#ani.save('animation.gif', writer='imagemagick', fps=30) # will be huge for ORNL
plt.show()


