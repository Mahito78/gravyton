import numpy as np


class planet():


    def __init__(self, name, mass, radius):
        self.name = name
        self.mass = mass
        self.radius = radius

    def density(self):
        return self.mass / (4/3 * np.pi * self.radius**3)
    
    def gravity_acceleration(self, distance):
        G = 6.67430e-11
        return G*self.masss / distance**2