import sys
from argparse import ArgumentParser
from matplotlib import animation
from matplotlib import pyplot as plt
from flock import Flock
from animator import FlockAnimator

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
        animator = FlockAnimator((-500,1500), (-500,1500), "The Boids!", boids)
        animator.animate_flock()
    except IOError:
        print "The file you provided does not exist.\n" 
        parser.print_help()
    except:
        print "Unexpected error.", sys.exc_info()[0], "\n"
        raise


if __name__ == "__main__":
    process()

