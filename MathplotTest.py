import matplotlib.pyplot as plt
import numpy as np
def inputxy(n):
    if n == "x":
        x = int(input("X = "))
        return x
    if n == "y":
        y = int(input("Y = "))
        return y

xpoints = np.array([])#posição X;
ypoints = np.array([])#posição Y dos pontos
x = []
y = []
for i in range(2):
    x = np.array([inputxy("x")])
    y = np.array([inputxy("y")])
    np.concatenate((xpoints, x))
    np.concatenate((ypoints, y))
#plt.plot(xpoints, ypoints)#Draw lines
plt.plot(xpoints, ypoints, 'o')
plt.show()