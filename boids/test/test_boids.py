from nose.tools import assert_almost_equal, assert_equal
import os
import yaml
import numpy as np
from .. import flock as fl

# Testing fly towards the middle
def test_fly_towards_the_middle():
    # Fixture file
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fly_towards_middle.yaml')))
    boid_data = regression_data["before"]

    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
        
    boids = fl.Flock("config.yaml")
    boids.set_positions(positions)
    boids.set_velocities(velocities)
    # Call method
    boids.fly_towards_the_middle()
    # Boid data after update
    boid_data_after = np.append(boids.positions, boids.velocities, axis=0) 
    
    for after,before in zip(regression_data["after"], boid_data_after):
        for after_value,before_value in zip(after, before): 
            assert_almost_equal(after_value, before_value, delta=0.1)

# Testing fly away from nearby boids
def test_fly_away_from_nearby_boids():
    # Fixture file
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fly_away_from_nearby_boids.yaml')))
    boid_data = regression_data["before"]

    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
        
    boids = fl.Flock("config.yaml")
    boids.set_positions(positions)
    boids.set_velocities(velocities)
    # Call method
    boids.fly_away_from_nearby_boids()
    # Boid data after update
    boid_data_after = np.append(boids.positions, boids.velocities, axis=0) 
    
    for after,before in zip(regression_data["after"], boid_data_after):
        for after_value,before_value in zip(after, before): 
            assert_almost_equal(after_value, before_value, delta=0.1)

# Testing match speed with nearby boids 
def test_match_speed_with_nearby_boids():
    # Fixture file
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/match_speed_with_nearby_boids.yaml')))
    boid_data = regression_data["before"]

    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
        
    boids = fl.Flock("config.yaml")
    boids.set_positions(positions)
    boids.set_velocities(velocities)
    # Call method
    boids.match_speed_with_nearby_boids()
    # Boid data after update
    boid_data_after = np.append(boids.positions, boids.velocities, axis=0) 
    
    for after,before in zip(regression_data["after"], boid_data_after):
        for after_value,before_value in zip(after, before): 
            assert_almost_equal(after_value, before_value, delta=0.1)

# Testing move according to velocities
def test_move_according_to_velocities():
    # Fixture file
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/move_according_to_velocities.yaml')))
    boid_data = regression_data["before"]

    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)

    boids = fl.Flock("config.yaml")
    boids.set_positions(positions)
    boids.set_velocities(velocities)
    # Call method
    boids.move_according_to_velocities()
    # Boid data after update
    boid_data_after = np.append(boids.positions, boids.velocities, axis=0)

    for after,before in zip(regression_data["after"], boid_data_after):
        for after_value,before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.1)


# Testing update boids
def test_update_boids():
    # Fixture file
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/update_boids.yaml')))
    boid_data = regression_data["before"]

    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)

    boids = fl.Flock("config.yaml")
    boids.set_positions(positions)
    boids.set_velocities(velocities)
    # Call method
    boids.update_boids()
    # Boid data after update
    boid_data_after = np.append(boids.positions, boids.velocities, axis=0)

    for after,before in zip(regression_data["after"], boid_data_after):
        for after_value,before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.1)


# Test compute square distances
def test_compute_square_distances():
    initial = np.zeros((2,50,50)) + 1
    final = np.zeros((50,50)) + 2
    
    boids = fl.Flock("config.yaml")
    # Call method
    final_after = boids.compute_square_distances(initial)
    for pos_final, pos_final_after in zip(final, final_after):
        for pos_final_val, pos_final_after_val in zip(pos_final, pos_final_after):
            assert_equal(pos_final_val, pos_final_after_val)

# Test setter for positions
def test_set_positions():
    initial = np.zeros((2,50,50)) + 1
    
    boids = fl.Flock("config.yaml")
    # Call method
    boids.set_positions(initial)
    
    for pos_initial, pos_after in zip(initial, boids.positions):
        for initial, after in zip(pos_initial, pos_after):
            for initial_val, after_val in zip(initial, after):
                assert_equal(initial_val, after_val)


# Test setter for velocities
def test_set_velocities():
    initial = np.zeros((2,50,50)) + 1
    
    boids = fl.Flock("config.yaml")
    # Call method
    boids.set_velocities(initial)
    
    for vel_initial, vel_after in zip(initial, boids.velocities):
        for initial, after in zip(vel_initial, vel_after):
            for initial_val, after_val in zip(initial, after):
                assert_equal(initial_val, after_val)














