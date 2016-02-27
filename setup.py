from setuptools import setup, find_packages

setup(
    name = "Boids",
    version = "1.0",
    description = "The Boids!",
    author = "Irina Grigorescu",
    author_email = "irina.grigorescu.15@ucl.ac.uk",
    url = "https://github.com/irinagrigorescu/bad_boids",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/boids'],
    install_requires = ['argparse', 'numpy', 'matplotlib']
)
