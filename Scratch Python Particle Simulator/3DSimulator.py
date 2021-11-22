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
elev = 30
azim = 30

xlim = (0,size)
ylim = (0,size)
zlim = (0,size)

# number of partitions in grid to zoom in on particle dynamics
grid_partition = 2

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_zlim(zlim)

ax.view_init(elev, azim)

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
        if self.xyz[0] <= xlim[0]:
            self.v[0] = cor * np.abs(self.v[0])

        # particle hits upper x wall
        elif self.xyz[0] >= xlim[1]:
            self.v[0] = - cor * np.abs(self.v[0])

        # particle hits lower y wall
        if self.xyz[1] <= ylim[0]:
            self.v[1] = cor * np.abs(self.v[1])

        # particle hits upper y wall
        elif self.xyz[1] >= ylim[1]:
            self.v[1] = - cor * np.abs(self.v[1])

        # particle hits lower z wall
        if self.xyz[2] <= zlim[0]:
            self.v[2] = cor * np.abs(self.v[2])

        # particle hits upper z wall
        elif self.xyz[2] >= zlim[1]:
            self.v[2] = - cor * np.abs(self.v[2])

        # changing velocity due to acceleration of gravity
        delta_v = delta_t * ag
        self.v += delta_v
        collision_info = self.does_elastic_collision_occur()
        if (collision_info[0]):
            self.deal_with_elastic_collision(collision_info[1])
        update_position(in_particle = self, g = grid)
        print("we are here")
        quit()
        # make sure the particles stay inside of the canvas
        self.xyz[0] = np.clip(self.xyz[0], xlim[0], xlim[1])
        self.xyz[1] = np.clip(self.xyz[1], ylim[0], ylim[1])
        self.xyz[2] = np.clip(self.xyz[2], zlim[0], zlim[1])

        # draw particle
        self.scatter.set_xdata(self.xyz[0])
        self.scatter.set_ydata(self.xyz[1])
        self.scatter.set_3d_properties(self.xyz[2])

def update_position(in_particle = None, g = None):
    # update grid here
    x = in_particle.xyz[0]
    y = in_particle.xyz[1]
    print(g[math.floor(x)][math.floor(y)])
    print(in_particle)

    g[math.floor(x)][math.floor(y)].remove(in_particle)
    new_x, new_y = x + in_particle.v[0]*TIME_STEP, y + in_particle.v[1]*TIME_STEP
    # try:
    g[math.floor(new_x)][math.floor(new_y)].append(in_particle)
    print('updated')
    quit()
        
    # except IndexError:
    #     print("x: " + str(math.floor(new_x)))
    #     print("y: " + str(math.floor(new_y)))
    #     print(g[new_x][new_y])
    in_particle.xyz[0] = new_x
    in_particle[1] = new_y

    pass  
        
def fill_grid(g = None, ep = None):
    for p in ep:
        x = math.floor(p.xyz[0])
        y = math.floor(p.xyz[1])
        g[x][y].append(p)
    pass

def init():
    return [] 

def update(t):

    global elev, azim

    for particle in particles:
        particle.update(grid)

    artists = [particle.scatter for particle in particles]
  
    # rotate view
    azim = azim + t/2
    ax.view_init(elev, azim)
    
    artists.append(ax)

    return artists

    # generate particles with random position, velocity, and color

for i in np.arange(0,num_particles):
    xyz = np.random.rand(1,3)[0]*size
    xyz[1] = 5 # for 2 dimensional dynamics
    v = np.random.rand(1,3)[0]*0.1
    v[1] = 0 # for 2 dimensional dynamics
    fmt = str(colors[np.random.randint(0,len(colors))] + 'o')
    particles.append(particle(xyz, v, fmt))

grid = [[list() for y in range (ylim[0], ylim[1])] for x in range (xlim[0], xlim[1])] # for efficient computation
fill_grid(g = grid, ep = particles)
print(grid)
ani = FuncAnimation(fig, update, frames=np.arange(0,0.5,delta_t), init_func=init, interval=10, blit=True, repeat=True)
#ani.save('animation.gif', writer='imagemagick', fps=30) # will be huge for ORNL
plt.show()





