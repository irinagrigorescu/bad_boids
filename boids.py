"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Global Parameters
NO_BOIDS = 50
MOVEMENT_STRENGTH = 0.01
ALERT_DISTANCE = 100
FORMATION_FLYING_DISTANCE = 10000
FORMATION_FLYING_STRENGTH = 0.125

# Deliberately terrible code for teaching purposes

boids_x=[random.uniform(-450,50.0) for x in range(NO_BOIDS)]
boids_y=[random.uniform(300.0,600.0) for x in range(NO_BOIDS)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(NO_BOIDS)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(NO_BOIDS)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

# Fly towards the middle function
def fly_towards_the_middle(boids):
	boid_pos_x,boid_pos_y,boid_vel_x,boid_vel_y = boids
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			attenuation_factor = MOVEMENT_STRENGTH/NO_BOIDS
			separation_x = boid_pos_x[j] - boid_pos_x[i]
			separation_y = boid_pos_y[j] - boid_pos_y[i]
			boid_vel_x[i] = boid_vel_x[i] + separation_x * attenuation_factor
			boid_vel_y[i] = boid_vel_y[i] + separation_y * attenuation_factor

# Fly away from nearby boids function
def fly_away_from_neaby_boids(boids):
	boid_pos_x,boid_pos_y,boid_vel_x,boid_vel_y = boids
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			separation_x = boid_pos_x[j] - boid_pos_x[i]
			separation_y = boid_pos_y[j] - boid_pos_y[i]
			squared_displacement_x = separation_x**2
			squared_displacement_y = separation_y**2
			square_distances = squared_displacement_x + squared_displacement_y
			if square_distances < ALERT_DISTANCE:
				boid_vel_x[i] = boid_vel_x[i] + separation_x
				boid_vel_y[i] = boid_vel_y[i] + separation_y
				
# Match speed with nearby boids
def match_speed_with_nearby_boids(boids):
	boid_pos_x,boid_pos_y,boid_vel_x,boid_vel_y = boids
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			separation_x = boid_pos_x[j] - boid_pos_x[i]
			separation_y = boid_pos_y[j] - boid_pos_y[i]
			squared_displacement_x = separation_x**2
			squared_displacement_y = separation_y**2
			velocity_difference_x = boid_vel_x[j]-boid_vel_x[i]
			velocity_difference_y = boid_vel_y[j]-boid_vel_y[i]
			square_distances = squared_displacement_x + squared_displacement_y
			if square_distances < FORMATION_FLYING_DISTANCE:
				boid_vel_x[i] = boid_vel_x[i] + velocity_difference_x * FORMATION_FLYING_STRENGTH/NO_BOIDS
				boid_vel_y[i] = boid_vel_y[i] + velocity_difference_y * FORMATION_FLYING_STRENGTH/NO_BOIDS

# Move according to velocities
def move_according_to_velocities(boids):
	boid_pos_x,boid_pos_y,boid_vel_x,boid_vel_y = boids
	for i in range(NO_BOIDS):
		boid_pos_x[i] = boid_pos_x[i] + boid_vel_x[i]
		boid_pos_y[i] = boid_pos_y[i] + boid_vel_y[i]
	
# Update boids function
def update_boids(boids):
	
	# Fly towards the middle
	fly_towards_the_middle(boids)
	
	# Fly away from nearby boids
	fly_away_from_neaby_boids(boids)
	
	# Try to match speed with nearby boids
	match_speed_with_nearby_boids(boids)
	
	# Move according to velocities
	move_according_to_velocities(boids)


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
