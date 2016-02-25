"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import sys

# Global Parameters
NO_BOIDS = 50
MOVEMENT_STRENGTH = 0.01
ALERT_DISTANCE = 100
FORMATION_FLYING_DISTANCE = 10000
FORMATION_FLYING_STRENGTH = 0.125
ATTENUATION_FACTOR = MOVEMENT_STRENGTH/NO_BOIDS

# Limits:
lower_limits_pos = np.array([-450.0, 300.0])
upper_limits_pos = np.array([  50.0, 600.0])
lower_limits_vel = np.array([   0.0, -20.0])
upper_limits_vel = np.array([  10.0,  20.0])

# Initialise flock positions and velocities 
def new_flock(lower_limits_pos, upper_limits_pos):
	width = upper_limits_pos - lower_limits_pos
	return (lower_limits_pos[:, np.newaxis] + np.random.rand(2, NO_BOIDS) * width[:, np.newaxis])
	

# Fly towards the middle function
def fly_towards_the_middle(positions, velocities):
	flock_middle = np.mean(positions, 1)
	direction_to_flock_middle = positions - flock_middle[:, np.newaxis]
	# Update velocities
	velocities -= direction_to_flock_middle * MOVEMENT_STRENGTH

# Fly away from nearby boids function
def fly_away_from_neaby_boids(positions, velocities):
	# Compute distances between boids
	separation_all = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
	squared_displacement_all = np.power(separation_all, 2)
	square_distances_all = np.sum(squared_displacement_all, 0)
	# Don't update for too close
	separations_far = np.copy(separation_all)
	far_index = (square_distances_all > ALERT_DISTANCE)
	separations_far[0,:,:][far_index] = 0
	separations_far[1,:,:][far_index] = 0
	# Update velocities
	velocities += np.sum(separations_far,1)
	
				
# Match speed with nearby boids
def match_speed_with_nearby_boids(positions, velocities):
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			separation = positions[:,j] - positions[:,i]
			squared_displacement = np.power(separation, 2)
			velocity_difference = velocities[:, j] - velocities[:, i]
			square_distances = np.sum(squared_displacement)
			if square_distances < FORMATION_FLYING_DISTANCE:
				velocities[:, i] = velocities[:, i] + velocity_difference * FORMATION_FLYING_STRENGTH/NO_BOIDS

# Move according to velocities
def move_according_to_velocities(positions, velocities):
	for i in range(NO_BOIDS):
		positions[:, i] = positions[:, i] + velocities[:, i]
	
# Update boids function
def update_boids(positions, velocities):
	
	# Fly towards the middle
	fly_towards_the_middle(positions, velocities)
	
	# Fly away from nearby boids
	fly_away_from_neaby_boids(positions, velocities)
	
	# Try to match speed with nearby boids
	match_speed_with_nearby_boids(positions, velocities)
	
	# Move according to velocities
	move_according_to_velocities(positions, velocities)


# Initialisations
positions  = new_flock(lower_limits_pos, upper_limits_pos)
velocities = new_flock(lower_limits_vel, upper_limits_vel)
#print positions
#sys.exit(0)

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(positions[0,:], positions[1,:])

def animate(frame):
   update_boids(positions, velocities)
   scatter.set_offsets(positions.transpose())

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
