from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
import numpy as np



class Simulation:
    def __init__(self, k, e, m):
        """
        Simulation variables
        """
        self.k = k
        self.e = e # [Joules]
        self.m = m # [Kilos]
        self.w = 0.01

        self.__figures = []
    def figures(self):
        return self.__figures
    
    def graph(self):
        self.__figures = []
        fig, axes = plt.subplots(2, 2, constrained_layout=True)
        axes[0][0].set_title("Speed !")
        t = np.arange(0, np.pi * 2, self.w) #[0,0.01,0.02,0.03,....3]
        axes[0][0].plot(t,  np.sin(t))
        self.__figures.append(fig) 
