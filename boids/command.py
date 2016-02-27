import sys
from argparse import ArgumentParser
from matplotlib import animation
from matplotlib import pyplot as plt
from flock import Flock

# Command line entry point
def process():
    parser = ArgumentParser(description = \
            "Simulate the motion of a flock of birds")
    
    # Parameters
    parser.add_argument('--file', '-f', dest = 'configFile')

    # Print help message even if no flag is provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    # Catch exception if file does not exist
    try:
        # Create object
        boids = Flock(args.configFile)
        # Plot figures
        figure = plt.figure()
        axes = plt.axes(xlim = (-500,1500), ylim = (-500,1500))
        scatter = axes.scatter(boids.positions[0,:], boids.positions[1,:])
        # Function handle for animate
        funcEval = lambda x: animate(boids, scatter)
        # Animate
        anim = animation.FuncAnimation(figure, funcEval, frames=50, interval=50)
        plt.show()
    except IOError:
        print "The file you provided does not exist.\n" 
        parser.print_help()
    except:
        print "Unexpected error.\n"


def animate(boids, scatter):
    boids.update_boids()
    scatter.set_offsets(boids.positions.transpose())

if __name__ == "__main__":
    process()

