"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Parameters
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

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*MOVEMENT_STRENGTH/NO_BOIDS
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*MOVEMENT_STRENGTH/NO_BOIDS
	# Fly away from nearby boids
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < ALERT_DISTANCE:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(NO_BOIDS):
		for j in range(NO_BOIDS):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < FORMATION_FLYING_DISTANCE:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*FORMATION_FLYING_STRENGTH/NO_BOIDS
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*FORMATION_FLYING_STRENGTH/NO_BOIDS
	# Move according to velocities
	for i in range(NO_BOIDS):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


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
