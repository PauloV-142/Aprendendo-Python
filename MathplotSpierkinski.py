'''
  WARNING: The scripts f2py and numpy-config are installed in '/var/data/python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts fonttools, pyftmerge, pyftsubset and ttx are installed in '/var/data/python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.v
'''
import matplotlib.pyplot as plt
import numpy as np
def inputx():
    x = int(input("X = "))
    return x
def inputy():
    y = int(input("Y = "))
    return y
a = [-200, -150]
b = [0, 150]
c = [200, -150]
xpoints = np.array([a[0], b[0], c[0]])#posição X;
ypoints = np.array([a[1], b[1], c[1]])#posição Y dos pontos
plt.plot(xpoints, ypoints, 'o')

def start():
    x = 0
    y = 0
    for i in range(50000):#Don't be scared, there will be 50 seconds of pure thinking, wait and you'll see!
        r = np.random.randint(3)
        match r:
            case 0:
                x = ((x - a[0])/2) + a[0]
                y = ((y - a[1])/2) + a[1]
            case 1:
                x = ((x - b[0])/2) + b[0]
                y = ((y - b[1])/2) + b[1]
            case 2:
                x = ((x - c[0])/2) + c[0]
                y = ((y - c[1])/2) + c[1]
                print(i)
        printerx = np.array([x])
        printery = np.array([y])
        #print(x, y, r)
        plt.plot(printerx, printery, marker = ',')

plt.grid(linestyle = '--', linewidth = 0.5)
start()
plt.show()
