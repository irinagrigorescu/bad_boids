from argparse import ArgumentParser
import sys
import yaml
import numpy as np
import flock as fl

# Fly towards the middle fixture file generator 
def record_fixture_fly_towards_the_middle(config_file, fixture_file):
    # Initial positions
    boids = fl.Flock(config_file)
    positions  = boids.get_positions().tolist()
    velocities = boids.get_velocities().tolist()

    # Call method
    boids.fly_towards_the_middle()

    # Updated positions
    positions_after = boids.get_positions().tolist()
    velocities_after = boids.get_velocities().tolist()
    
    positions.extend(velocities)
    positions_after.extend(velocities_after)

    fixture = {"before": positions, "after": positions_after}
    fixture_file_handle = open(fixture_file, 'w')
    fixture_file_handle.write(yaml.dump(fixture))
    fixture_file_handle.close()
    
# Fly away from nearby boids fixture file generator 
def record_fixture_fly_away_from_nearby_boids(config_file, fixture_file):
    # Initial positions
    boids = fl.Flock(config_file)
    positions  = boids.get_positions().tolist()
    velocities = boids.get_velocities().tolist()

    # Call method
    boids.fly_away_from_nearby_boids()

    # Updated positions
    positions_after = boids.get_positions().tolist()
    velocities_after = boids.get_velocities().tolist()
    
    positions.extend(velocities)
    positions_after.extend(velocities_after)

    fixture = {"before": positions, "after": positions_after}
    fixture_file_handle = open(fixture_file, 'w')
    fixture_file_handle.write(yaml.dump(fixture))
    fixture_file_handle.close()

# Match speed with nearby boids fixture file generator
def record_fixture_match_speed_with_nearby_boids(config_file, fixture_file):
    # Initial positions
    boids = fl.Flock(config_file)
    positions  = boids.get_positions().tolist()
    velocities = boids.get_velocities().tolist()

    # Call method
    boids.match_speed_with_nearby_boids()

    # Updated positions
    positions_after = boids.get_positions().tolist()
    velocities_after = boids.get_velocities().tolist()
    
    positions.extend(velocities)
    positions_after.extend(velocities_after)

    fixture = {"before": positions, "after": positions_after}
    fixture_file_handle = open(fixture_file, 'w')
    fixture_file_handle.write(yaml.dump(fixture))
    fixture_file_handle.close()

# Move according to velocities fixture file generator
def record_fixture_move_according_to_velocities(config_file, fixture_file):
    # Initial positions
    boids = fl.Flock(config_file)
    positions  = boids.get_positions().tolist()
    velocities = boids.get_velocities().tolist()

    # Call method
    boids.move_according_to_velocities()

    # Updated positions
    positions_after = boids.get_positions().tolist()
    velocities_after = boids.get_velocities().tolist()
    
    positions.extend(velocities)
    positions_after.extend(velocities_after)

    fixture = {"before": positions, "after": positions_after}
    fixture_file_handle = open(fixture_file, 'w')
    fixture_file_handle.write(yaml.dump(fixture))
    fixture_file_handle.close()
 
# Update boids fixture file generator
def record_fixture_update_boids(config_file, fixture_file):
    # Initial positions
    boids = fl.Flock(config_file)
    positions  = boids.get_positions().tolist()
    velocities = boids.get_velocities().tolist()

    # Call method
    boids.update_boids()

    # Updated positions
    positions_after = boids.get_positions().tolist()
    velocities_after = boids.get_velocities().tolist()
    
    positions.extend(velocities)
    positions_after.extend(velocities_after)

    fixture = {"before": positions, "after": positions_after}
    fixture_file_handle = open(fixture_file, 'w')
    fixture_file_handle.write(yaml.dump(fixture))
    fixture_file_handle.close()
 
# Function that generates all the fixture files
def record_fixtures(config_file, fixture_dest):
    # Create list of fixture file names
    fixture_files = ['fly_towards_middle', \
                     'fly_away_from_nearby_boids', \
                     'match_speed_with_nearby_boids', \
                     'move_according_to_velocities', \
                     'update_boids']
    # Add destination folder and .yaml termination to the whole list
    concat = lambda name: fixture_dest + '/' + name + '.yaml'
    fixture_files = list(map(concat, fixture_files))

    # Call record fixtures
    record_fixture_fly_towards_the_middle(config_file, fixture_files[0])
    record_fixture_fly_away_from_nearby_boids(config_file, fixture_files[1])
    record_fixture_match_speed_with_nearby_boids(config_file, fixture_files[2])
    record_fixture_move_according_to_velocities(config_file, fixture_files[3])
    record_fixture_update_boids(config_file, fixture_files[4])

if __name__ == "__main__":
    parser = ArgumentParser(description = "Generate fixture files")
    
    # Parameters
    parser.add_argument('--configFile', '-cf', dest = 'configFile')
    parser.add_argument('--fixtureDest', '-fd', dest = 'fixtureDest')

    # Print help message even if no flag is provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    record_fixtures(args.configFile, args.fixtureDest)
