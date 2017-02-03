import numpy as np

class Data:
    def __init__(self):
        self.index = np.linspace(0, 10, 11)

    def signal(self, index):     
        t = np.linspace(0, 10, 11)
        return np.sin(2*np.pi*index*t)
    
    def signal2D(self, index):
        t = np.linspace(-10, 10, 11)
        X, Y = np.meshgrid(t, t)
        return np.sin(2*np.pi*index*(X**2 + Y**2))
