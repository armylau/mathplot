'''
Draw 3d surface
'''

import numpy as np
from matplotlib import pyplot as plt


def plot_linear_line():
    x = np.arange(1, 11)
    y = 2 * x + 5
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y)
    plt.show()

def plot_3dtest():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X = np.arange(-10, 10, 0.25)
    Y = np.arange(-10, 10, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = (X**2 + Y**2) * (1.0 / 20.0 )

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                           linewidth=0, antialiased=False)
    ax.set_zlim(-1, 1)

    plt.show()

if __name__ == '__main__':
    plot_3dtest()