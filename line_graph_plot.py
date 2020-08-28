import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x,y,'r')

plt.title("Basic Line Graph")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.grid(True)
plt.show()