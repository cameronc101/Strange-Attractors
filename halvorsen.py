import numpy as np
import matplotlib.pyplot as plt

steps = 100000
dt = 0.005
a = 1.4
x = 0.1
y = 0
z = 0

points_x = [x]
points_y = [y]
points_z = [z]

for _ in range(steps):
    dx = -a * x - 4 * y - 4 * z - y * y
    dy = -a * y - 4 * z - 4 * x - z * z
    dz = -a * z - 4 * x - 4 * y - x * x
    x += dx * dt
    y += dy * dt
    z += dz * dt
    points_x.append(x)
    points_y.append(y)
    points_z.append(z)
    print(str(x) + " " + str(y) + " " + str(z))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax._axis3don = False
ax.set_facecolor('#222222')
plt.title('Halvorsen Attractor')
ax.plot(points_x,points_y,points_z,color='#cccccc',linewidth=0.1)
plt.show()