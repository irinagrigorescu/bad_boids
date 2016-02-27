"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""
import numpy as np
import sys
import yaml
from matplotlib import animation

class Flock(object):
	def __init__(self, config_file):
		# Config file manipulation
		self.config = yaml.load(open(config_file))
		lower_limits_pos = np.array(self.config['LOWER_LIM_POS'])
		upper_limits_pos = np.array(self.config['UPPER_LIM_POS'])
		lower_limits_vel = np.array(self.config['LOWER_LIM_VEL'])
		upper_limits_vel = np.array(self.config['UPPER_LIM_VEL'])
		# Positions and velocities
		self.positions  = self.generate_initial_positions(lower_limits_pos, upper_limits_pos)
		self.velocities = self.generate_initial_positions(lower_limits_vel, upper_limits_vel)
	
	# Fly towards the middle function
	def fly_towards_the_middle(self):
		flock_middle = np.mean(self.positions, 1)
		direction_to_flock_middle = self.positions - flock_middle[:, np.newaxis]
		# Update velocities
		self.velocities -= direction_to_flock_middle * self.config['MOVEMENT_STRENGTH']
		
	# Fly away from nearby boids function
	def fly_away_from_nearby_boids(self):
		# Compute distances between boids
		separation_all = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
		square_distances_all = self.compute_square_distances(separation_all)
		# Don't update if too far
		separations_far = np.copy(separation_all)
		far_index = (square_distances_all > self.config['ALERT_DISTANCE'])
		separations_far[0,:,:][far_index] = 0
		separations_far[1,:,:][far_index] = 0
		# Update velocities
		self.velocities += np.sum(separations_far,1)

	# Match speed with nearby boids
	def match_speed_with_nearby_boids(self):
		# Compute difference between velocities
		velocities_dif_all = self.velocities[:,np.newaxis,:] - self.velocities[:,:,np.newaxis]
		separation_all = self.positions[:,np.newaxis,:] - self.positions[:,:,np.newaxis]
		square_distances_all = self.compute_square_distances(separation_all)
		# Match speed only with the closest ones
		velocities_far = np.copy(velocities_dif_all)
		far_index = (square_distances_all > self.config['FORMATION_FLYING_DISTANCE'])
		velocities_far[0,:,:][far_index] = 0
		velocities_far[1,:,:][far_index] = 0	
		# Update velocities
		self.velocities -= np.mean(velocities_far, 1) * self.config['FORMATION_FLYING_STRENGTH']

	# Move according to velocities
	def move_according_to_velocities(self):
		self.positions += self.velocities

	# Update boids function
	def update_boids(self):
		self.fly_towards_the_middle()
		self.fly_away_from_nearby_boids()
		self.match_speed_with_nearby_boids()
		self.move_according_to_velocities()

	# Initialise flock positions and velocities 
	def generate_initial_positions(self, lower_limits_pos, upper_limits_pos):
		width = upper_limits_pos - lower_limits_pos
		return (lower_limits_pos[:, np.newaxis] + np.random.rand(2, self.config['NO_BOIDS']) * width[:, np.newaxis])
	
	# Compute square distances
	def compute_square_distances(self, separation_all):
		squared_displacement_all = np.power(separation_all, 2)
		square_distances_all = np.sum(squared_displacement_all, 0)
		return square_distances_all
		
	# Setter for positions
	def set_positions(self, new_positions):
		self.positions = new_positions
	
	# Setter for velocities
	def set_velocities(self, new_velocities):
		self.velocities = new_velocities
		
	


'''
# Create Object	
boids = Flock("config.yaml")

# Plot figures
figure = plt.figure()
axes = plt.axes(xlim = (-500,1500), ylim = (-500,1500))
scatter = axes.scatter(boids.positions[0,:], boids.positions[1,:])

def animate(frame):
   boids.update_boids()
   scatter.set_offsets(boids.positions.transpose())

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
'''
