import numpy as np

a = np.empty((10, 10))
# print(a)

b = [[list() for x in range(10)] for y in range (10)]
b[7][4].append("yeets")
b[7][4].remove("yeets")
print (b[7][4])

