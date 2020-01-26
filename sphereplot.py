import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a sphere
r = 1 #adjust as needed
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)

#Import data
data = np.genfromtxt('line.txt') #replace this with your data, .txt is required but it should be fine. or you can use pandas library to read a csv, something like that
theta, phi, r = np.hsplit(data, 3) 
theta = theta * pi / 180.0
phi = phi * pi / 180.0
xx = sin(phi)*cos(theta)
yy = sin(phi)*sin(theta)
zz = cos(phi)

#a quick rough way to add extra lines, just uncomment as needed
# data2 = np.genfromtxt('line2.txt') #replace this with your data, .txt is required but it should be fine. or you can use pandas library to read a csv, something like that
# theta2, phi2, r2 = np.hsplit(data2, 3) 
# theta2 = theta2 * pi / 180.0
# phi2 = phi2 * pi / 180.0
# xx2 = sin(phi2)*cos(theta2)
# yy2 = sin(phi2)*sin(theta2)
# zz2 = cos(phi2)

#a quick rough way to add extra lines, just uncomment as needed
# data3 = np.genfromtxt('line3.txt') #replace this with your data, .txt is required but it should be fine. or you can use pandas library to read a csv, something like that
# theta3, phi3, r3 = np.hsplit(data, 3) 
# theta3 = theta3 * pi / 180.0
# phi3 = phi3 * pi / 180.0
# xx3 = sin(phi3)*cos(theta3)
# yy3 = sin(phi3)*sin(theta3)
# zz3 = cos(phi3)

#Set colours and render
fig = plt.figure(figsize=plt.figaspect(1)*1) #Adjusts the aspect ratio and enlarges the figure (text does not enlarge)
ax = fig.gca(projection='3d')

#a quick rough way to add extra lines, just uncomment as needed
#ax2 = fig.gca(projection='3d')
#ax3 = fig.gca(projection='3d')

ax.plot_surface(
    x, y, z,  rstride=1, cstride=1, color='c', alpha=0.3, linewidth=0) #change the alpha transparency, color etc. as needed

#a quick rough way to add extra lines, just uncomment as needed
# ax2.plot_surface(
#     x, y, z,  rstride=1, cstride=1, color='c', alpha=0.3, linewidth=0) #change the alpha transparency, color etc. as needed
# ax3.plot_surface(
#     x, y, z,  rstride=1, cstride=1, color='c', alpha=0.3, linewidth=0) #change the alpha transparency, color etc. as needed

ax.scatter(xx,yy,zz,color="k",s=20)
ax.plot_wireframe(xx, yy, zz)

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.set_zlim([-1,1])

#a quick rough way to add extra lines, just uncomment as needed
# ax2.scatter(xx,yy,zz,color="k",s=20)
# ax2.plot_wireframe(xx, yy, zz)

# ax2.set_xlim([-1,1])
# ax2.set_ylim([-1,1])
# ax2.set_zlim([-1,1])

#a quick rough way to add extra lines, just uncomment as needed
# ax3.scatter(xx,yy,zz,color="k",s=20)
# ax3.plot_wireframe(xx, yy, zz)

# ax3.set_xlim([-1,1])
# ax3.set_ylim([-1,1])
# ax3.set_zlim([-1,1])

plt.tight_layout()
plt.show()