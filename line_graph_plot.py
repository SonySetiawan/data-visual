import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,10)
#np.linspace(start,end,num)
#num = jumlah generate sampling.
#https://numpy.org/doc/stable/reference/generated/numpy.linspace.html

plt.plot(x, x**2, '--r', label="square")
plt.plot(x, x**3, 'b', label="cube")

plt.xlim(0,10)
plt.ylim(0,1000)
plt.legend()

plt.title("Basic Line Graph")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.grid(True)
plt.show()