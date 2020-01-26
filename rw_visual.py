import matplotlib.pyplot as plt 
from random_walk import RandomWalk

while True:
    # Make a ramdom walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk 
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, edgecolors='none' ,s=15)
    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break