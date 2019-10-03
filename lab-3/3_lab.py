from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
fig = plt.figure()
ax = plt.axes(projection="3d")


def z_function(x, y):
    return (np.sin(np.sqrt(x ** 2 + y ** 2))) / np.sqrt(x ** 2 + y ** 2)


x = np.linspace(-6, 6, 40)
y = np.linspace(-6, 6, 40)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)
ax.plot_wireframe(X, Y, Z, color='blue')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap=cm.coolwarm, edgecolor='none')
ax.set_title('surface');
plt.show()
