"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import sys
import yaml

# Initialise flock positions and velocities 
def new_flock(lower_limits_pos, upper_limits_pos):
	width = upper_limits_pos - lower_limits_pos
	return (lower_limits_pos[:, np.newaxis] + np.random.rand(2, config['NO_BOIDS']) * width[:, np.newaxis])
	

# Fly towards the middle function
def fly_towards_the_middle(positions, velocities):
	flock_middle = np.mean(positions, 1)
	direction_to_flock_middle = positions - flock_middle[:, np.newaxis]
	# Update velocities
	velocities -= direction_to_flock_middle * config['MOVEMENT_STRENGTH']

def compute_square_distances(separation_all):
	squared_displacement_all = np.power(separation_all, 2)
	square_distances_all = np.sum(squared_displacement_all, 0)
	return square_distances_all

# Fly away from nearby boids function
def fly_away_from_nearby_boids(positions, velocities):
	# Compute distances between boids
	separation_all = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
	square_distances_all = compute_square_distances(separation_all)
	# Don't update if too far
	separations_far = np.copy(separation_all)
	far_index = (square_distances_all > config['ALERT_DISTANCE'])
	separations_far[0,:,:][far_index] = 0
	separations_far[1,:,:][far_index] = 0
	# Update velocities
	velocities += np.sum(separations_far,1)
	
				
# Match speed with nearby boids
def match_speed_with_nearby_boids(positions, velocities):
	# Compute difference between velocities
	velocities_dif_all = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
	separation_all = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
	square_distances_all = compute_square_distances(separation_all)
	# Match speed only with the closest ones
	velocities_far = np.copy(velocities_dif_all)
	far_index = (square_distances_all > config['FORMATION_FLYING_DISTANCE'])
	velocities_far[0,:,:][far_index] = 0
	velocities_far[1,:,:][far_index] = 0	
	# Update velocities
	velocities -= np.mean(velocities_far, 1) * config['FORMATION_FLYING_STRENGTH']
	
	
# Move according to velocities
def move_according_to_velocities(positions, velocities):
	for i in range(config['NO_BOIDS']):
		positions[:, i] += velocities[:, i]
	
# Update boids function
def update_boids(positions, velocities):
	
	# Fly towards the middle
	fly_towards_the_middle(positions, velocities)
	
	# Fly away from nearby boids
	fly_away_from_nearby_boids(positions, velocities)
	
	# Try to match speed with nearby boids
	match_speed_with_nearby_boids(positions, velocities)
	
	# Move according to velocities
	move_according_to_velocities(positions, velocities)



# Initialisations
config = yaml.load(open("config.yaml"))
lower_limits_pos = np.array(config['LOWER_LIM_POS'])
upper_limits_pos = np.array(config['UPPER_LIM_POS'])
lower_limits_vel = np.array(config['LOWER_LIM_VEL'])
upper_limits_vel = np.array(config['UPPER_LIM_VEL'])

positions  = new_flock(lower_limits_pos, upper_limits_pos)
velocities = new_flock(lower_limits_vel, upper_limits_vel)

# Plot figures
figure = plt.figure()
axes = plt.axes(xlim = (-500,1500), ylim = (-500,1500))
scatter = axes.scatter(positions[0,:], positions[1,:])

def animate(frame):
   update_boids(positions, velocities)
   scatter.set_offsets(positions.transpose())

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
