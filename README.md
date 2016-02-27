Bad Boids
=========

**Description:**

Refactoring the Bad Boids Assignment for the Research Software Engineering with Python module.

**Usage:**
```
usage: command.py [-h] [--file CONFIGFILE]

Simulate the motion of a flock of birds

optional arguments:
  -h, --help            show this help message and exit
    --file CONFIGFILE, -f CONFIGFILE
```

**Installation:**
```sudo pip install git+git://github.com/irinagrigorescu/bad_boids```

**Configuration File:**
In order to make the boids fly you will need a configuration file.
You can use this one as an example:
```
NO_BOIDS: 50
MOVEMENT_STRENGTH: 0.01
ALERT_DISTANCE: 100 
FORMATION_FLYING_DISTANCE: 10000
FORMATION_FLYING_STRENGTH: 0.125
LOWER_LIM_POS: [-450.0, 300.0]
UPPER_LIM_POS: [  50.0, 600.0]
LOWER_LIM_VEL: [   0.0, -20.0]
UPPER_LIM_VEL: [  10.0,  20.0]
```

For more information, you can contact me (Irina Grigorescu) at: irinagry@gmail.com
