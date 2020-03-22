import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from mpl_toolkits import mplot3d
from Bezier import Bezier
from numpy import array as a
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d

#Reto Interpolacion de mortero con curvas de Bezier
#Juan Camilo Chafloque, Abel Santiago Cortes, Sebastian Osorio

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

h = 0
b = 2
cg = 0
c = 0.55191502449

for i in range(0, 30):

	points_set_1 = a([[0 + b, 1 + b, 0 + h], [c + cg, 1 + b, 0 + h], [1 + b, c + cg, 0 + h], [1 + b, 0 + b, 0 + h], 
					[1 + b, 0 + b, 0 + h], [1 + b, -c - cg, 0 + h], [c + cg, -1 - b, 0 + h], [0 + b, -1 - b, 0 + h], 
					[0 + b, -1 - b, 0 + h], [-c - cg, -1 - b, 0 + h], [-1 - b, -c - cg, 0 + h], [-1 - b, 0 + b, 0 + h], 
					[-1 - b, 0 + b, 0 + h], [-1 - b, c + cg, 0 + h], [-c - cg, 1 + b, 0 + h], [0 + b, 1 + b, 0 + h]])
	t_points = np.arange(0, 1, 0.01)
	curve_set_1 = Bezier.Curve(t_points, points_set_1)
	if i == 0:
		p = Circle((0, 0), b, color="blue", fill=True)
	else:
		p = Circle((0, 0), b, color="blue", fill=False)
	ax.add_patch(p)
	art3d.pathpatch_2d_to_3d(p, z = h)
	
	b = b + 0.1
	h = h + 0.01

g = 7
x = 0
#Se dibuja la forma superior del mortero

for i in range(0, 10):
    
	points_set_1 = a([[-3, -4, h], [-1, -5.2 - x, h], [1, -5.2 - x, h], [3, -4, h]])
	t_points = np.arange(0, 1, 0.01)
	curve_set_1 = Bezier.Curve(t_points, points_set_1)
	ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2], color="blue")

	points_set_2 = a([[-3, 4, h], [-1, 5.2 + x, h], [1, 5.2 + x, h], [3, 4, h]])
	t_points = np.arange(0, 1, 0.01)
	curve_set_2 = Bezier.Curve(t_points, points_set_2)
	ax.plot(curve_set_2[:, 0], curve_set_2[:, 1], curve_set_2[:, 2], color="blue")

	points_set_3 = a([[4.2, 2.7, h], [5.2 + x, 1, h], [5.2 + x, -1, h], [4.2, -2.7, h]])
	t_points = np.arange(0, 1, 0.01)
	curve_set_3 = Bezier.Curve(t_points, points_set_3)
	ax.plot(curve_set_3[:, 0], curve_set_3[:, 1], curve_set_3[:, 2], color="blue")

	points_set_4 = a([[-4.2, -2.7, h], [-5.2 - x, -1, h], [-5.2 - x, 1, h], [-4.2, 2.7, h]])
	t_points = np.arange(0, 1, 0.01)
	curve_set_4 = Bezier.Curve(t_points, points_set_4)
	ax.plot(curve_set_4[:, 0], curve_set_4[:, 1], curve_set_4[:, 2], color="blue")

	#Juntar las curvas de la parte de arriba del mortero

	points_set_aux1 = a([[4.2, 2.7, h], [4.2, 2.7, h], [3, 4, h], [3, 4, h]])
	t_points = np.arange(0, 1, 0.01)
	curve_set_aux1 = Bezier.Curve(t_points, points_set_aux1)
	ax.plot(curve_set_aux1[:, 0], curve_set_aux1[:, 1], curve_set_aux1[:, 2], color="blue")

	points_set_aux2 = a([[-3, 4, h], [-3, 4, h], [-4.2, 2.7, h], [-4.2, 2.7, h]])
	t_points = np.arange(0, 1, 0.01)
	curve_set_aux2 = Bezier.Curve(t_points, points_set_aux2)
	ax.plot(curve_set_aux2[:, 0], curve_set_aux2[:, 1], curve_set_aux2[:, 2], color="blue")

	points_set_aux3 = a([[-4.2, -2.7, h], [-4.2, -2.7, h], [-3, -4, h], [-3, -4, h]])
	t_points = np.arange(0, 1, 0.01)
	curve_set_aux3 = Bezier.Curve(t_points, points_set_aux3)
	ax.plot(curve_set_aux3[:, 0], curve_set_aux3[:, 1], curve_set_aux3[:, 2], color="blue")

	points_set_aux4 = a([[3, -4, h], [3, -4, h], [4.2, -2.7, h], [4.2, -2.7, h]])
	t_points = np.arange(0, 1, 0.01)
	curve_set_aux4 = Bezier.Curve(t_points, points_set_aux4)
	ax.plot(curve_set_aux4[:, 0], curve_set_aux4[:, 1], curve_set_aux4[:, 2], color="blue")

	h = h + 0.01
	x = x + 0.20

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 1)
plt.show()