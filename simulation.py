import matplotlib.pyplot as plt
import numpy as np



class Simulation:
    def __init__(self, k, e, m):
        """
        Simulation variables (automatiquements rajoutées dans l'interface)
        """
        self.k = k
        self.e = e # [Joules]
        self.m = m # [Kilos]
        self.dt = 0.01

        self.__figures = []
    def figures(self):
        return self.__figures
    
    def graph(self):
        self.__figures = []
        fig, axes = plt.subplots(2, 2, constrained_layout=True)
        axes[0][0].set_title("Speed")
        t = np.arange(0, np.pi * 2, self.dt) #[0,0.01,0.02,0.03,....3]
        axes[0][0].plot(t,  np.sin(t), color="red")

        axes[0][1].set_title("Accélération")
        axes[0][1].plot(t,  np.cos(t))

        
        axes[1][0].set_title("Expo")
        axes[1][0].plot(t,  np.exp(t))

        axes[1][1].set_title("Log")
        axes[1][1].plot(t,  np.log(t))
        self.__figures.append(fig) 
