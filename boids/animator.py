import sys 
from argparse import ArgumentParser
from matplotlib import animation
from matplotlib import pyplot as plt 

class FlockAnimator(object):
    def __init__(self, plot_lim_x, plot_lim_y, title, flock_obj):
        self.xlim = plot_lim_x
        self.ylim = plot_lim_y
        self.title = title
        self.boids = flock_obj

    def animate_flock(self):
        figure = plt.figure()
        axes = plt.axes(xlim = self.xlim, ylim = self.ylim)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(self.title)
        scatter = axes.scatter(self.boids.positions[0,:], self.boids.positions[1,:])
        # Function handle for animate
        funcEval = lambda x: self.__animate(scatter)
        # Animate 
        anim = animation.FuncAnimation(figure, funcEval, frames=50, interval=50)
        plt.show()

    def __animate(self, scatter):
        self.boids.update_boids()
        scatter.set_offsets(self.boids.positions.transpose())


