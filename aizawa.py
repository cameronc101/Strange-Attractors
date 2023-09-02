import numpy as np
import matplotlib.pyplot as plt

steps = 100000
dt = 0.01
a = 0.95
b = 0.7
c = 0.6
d = 3.5
e = 0.25
f = 0.1
x = 0.1
y = 0
z = 0

points_x = [x]
points_y = [y]
points_z = [z]

for _ in range(steps):
    dx = (z - b) * x - d * y
    dy = d * x + (z - b) * y
    dz = c + a * z - (z ** 3 / 3) - (x ** 2 + y ** 2) * (1 + e * z) + f * z * x ** 3
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
plt.title('Aizawa Attractor')
ax.plot(points_x,points_y,points_z,color='#cccccc',linewidth=0.1)
plt.show()


