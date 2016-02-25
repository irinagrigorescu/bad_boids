from boids import update_boids
from nose.tools import assert_almost_equal
import os
import yaml
import numpy as np

def test_bad_boids_regression():
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data = regression_data["before"]

    positions  = np.append([np.asarray(boid_data[0])], [np.asarray(boid_data[1])], axis=0)
    velocities = np.append([np.asarray(boid_data[2])], [np.asarray(boid_data[3])], axis=0)

    update_boids(positions, velocities)
    boid_data_after = np.append(positions, velocities, axis=0) # boid data after update
    
    for after,before in zip(regression_data["after"], boid_data_after):
        for after_value,before_value in zip(after, before): 
            assert_almost_equal(after_value, before_value, delta=0.1)
