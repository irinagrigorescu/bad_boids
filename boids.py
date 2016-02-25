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

# Limits:
lower_limits_pos = np.array([-450.0, 300.0])
upper_limits_pos = np.array([  50.0, 600.0])
lower_limits_vel = np.array([   0.0, -20.0])
upper_limits_vel = np.array([  10.0,  20.0])

#boids_x=[random.uniform(-450,50.0) for x in range(NO_BOIDS)]
#boids_y=[random.uniform(300.0,600.0) for x in range(NO_BOIDS)]
#boid_x_velocities=[random.uniform(0,10.0) for x in range(NO_BOIDS)]
#boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(NO_BOIDS)]
#boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

# Initialise flock positions and velocities # sunt la schimbarea cu numpy adica refactoring nr 6 hand-written code 
def new_flock(lower_limits_pos, upper_limits_pos):
	width = upper_limits_pos - lower_limits_pos
	return (lower_limits_pos[:, np.newaxis] + np.random.rand(2, NO_BOIDS) * width[:, np.newaxis])
	

# Fly towards the middle function
def fly_towards_the_middle(positions, velocities):
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			attenuation_factor = MOVEMENT_STRENGTH/NO_BOIDS
			separation_x = positions[0][j] - positions[0][i]
			separation_y = positions[1][j] - positions[1][i]
			velocities[0][i] = velocities[0][i] + separation_x * attenuation_factor
			velocities[1][i] = velocities[1][i] + separation_y * attenuation_factor

# Fly away from nearby boids function
def fly_away_from_neaby_boids(positions, velocities):
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			separation_x = positions[0][j] - positions[0][i]
			separation_y = positions[1][j] - positions[1][i]
			squared_displacement_x = separation_x**2
			squared_displacement_y = separation_y**2
			square_distances = squared_displacement_x + squared_displacement_y
			if square_distances < ALERT_DISTANCE:
				velocities[0][i] = velocities[0][i] - separation_x
				velocities[1][i] = velocities[1][i] - separation_y
				
# Match speed with nearby boids
def match_speed_with_nearby_boids(positions, velocities):
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			separation_x = positions[0][j] - positions[0][i]
			separation_y = positions[1][j] - positions[1][i]
			squared_displacement_x = separation_x**2
			squared_displacement_y = separation_y**2
			velocity_difference_x = velocities[0][j] - velocities[0][i]
			velocity_difference_y = velocities[1][j] - velocities[1][i]
			square_distances = squared_displacement_x + squared_displacement_y
			if square_distances < FORMATION_FLYING_DISTANCE:
				velocities[0][i] = velocities[0][i] + velocity_difference_x * FORMATION_FLYING_STRENGTH/NO_BOIDS
				velocities[1][i] = velocities[1][i] + velocity_difference_y * FORMATION_FLYING_STRENGTH/NO_BOIDS

# Move according to velocities
def move_according_to_velocities(positions, velocities):
	for i in range(NO_BOIDS):
		positions[0][i] = positions[0][i] + velocities[0][i]
		positions[1][i] = positions[1][i] + velocities[1][i]
	
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
