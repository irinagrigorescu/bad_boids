from nose.tools import assert_almost_equal
import os
import yaml
import numpy as np
from .. import flock as fl

def test_bad_boids_regression():
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures/fixture.yml')))
    boid_data = regression_data["before"]

    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)
    
    boids = fl.Flock("../config.yaml")
    boids.set_positions(positions)
    boids.set_velocities(velocities)
    boids.update_boids()
    boid_data_after = np.append(boids.positions, boids.velocities, axis=0) # boid data after update
    
    for after,before in zip(regression_data["after"], boid_data_after):
        for after_value,before_value in zip(after, before): 
            assert_almost_equal(after_value, before_value, delta=0.1)
