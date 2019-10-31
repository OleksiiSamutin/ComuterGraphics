import math
import matplotlib.pyplot as plt
import numpy as np
def z_function(x, y):
    if (x or y)==0:
        return 1
    return (math.sin(math.sqrt(x ** 2 + y ** 2))) / math.sqrt(x ** 2 + y ** 2)


Xi = -6
Yi = -6
Zi = -6
Xarray = []
Yarray = []
while Xi < 6:
    Xi = round(Xi + 0.001, 4)

    while Yi < 6:

        result = round(z_function(Xi, Yi), 4)
        Yi = round(Yi + 0.001, 4)
        if result == 0.64:
            plt.scatter(Xi, Yi)

    Yi = -6

while Xi < 6:
    Xi = round(Xi + 0.001, 4)
    Xarray.append(Xi)
    Yarray.append(z_function(0, Xi))

a = np.array(Xarray)
b = np.array(Yarray)
#plt.plot(a, b)
plt.xlabel("X")
plt.ylabel("Z")
plt.bar(a, b)
plt.show()
