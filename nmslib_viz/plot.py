import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d


def show(data_set, number_points: int):
    """
    Visualize data set plotting the points with a certain amount of points as maximum.
    :param data_set: Set of points to plot.
    :param number_points: Amount of points maximum to show.
    :return: Data set plotted.
    """
    print(f'info: Showing {number_points} as maximum.')
    sub_set_points = np.random.choice(range(data_set.shape[0]), size=min(data_set.shape[0], number_points))
    x = data_set[sub_set_points, 0]
    y = data_set[sub_set_points, 1]
    z = data_set[sub_set_points, 2]

    fig = plt.figure(figsize=(8, 8))
    ax = mplot3d.Axes3D(fig)
    ax.set_title('NMSLIB index 3D representation', fontsize=20)
    ax.scatter(xs=x, ys=y, zs=z)
    plt.show()
