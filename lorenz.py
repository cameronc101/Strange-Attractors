import numpy as np
import matplotlib.pyplot as plt

steps = 100000
dt = 0.005
σ = 10
ρ = 28
β = 8.0/3.0
x = 2
y = 1
z = 1

points_x = [x]
points_y = [y]
points_z = [z]

for _ in range(steps):
    dx = σ * (y - x)
    dy = x * (ρ - z)
    dz = x * y - β * z
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
plt.title('Lorenz Attractor')
ax.plot(points_x,points_y,points_z,color='#cccccc',linewidth=0.1)
plt.show()


