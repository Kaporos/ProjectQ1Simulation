import matplotlib.pyplot as plt
import numpy as np
import math
class Simulation:
    def __init__(self):
        """
        Simulation variables (automatiquements rajoutées dans l'interface)
        """
        self.klanceur = 0.04
        self.ksol = 0.04
        self.rig = 20
        self.m = 0.250 # [Kilos]
        self.g = 9.81 #[m/s2] 
        self.time = 20 # [Seconds]
        self.dt = 0.01 # [Seconds]
        self.x = 0.60 # [Metres]

        self.__figures = []
    def figures(self):
        return self.__figures
    
    def graph(self, comparison_data):
        print(comparison_data)
        print(self.rig*self.x*self.x/2)

        self.__figures = []

        fig, axes = plt.subplots(2,2, constrained_layout=True) 

        t = np.arange(0, self.time, self.dt) #[0,0.01,0.02,0.03,....3]
        acc = np.full_like(t, -1*self.ksol*self.g)
        start_speed = np.full_like(t, math.sqrt(((self.rig*(self.x*self.x)) / self.m) - 2 * self.klanceur * self.g * self.x))
        speed = start_speed + acc * t
        move_evolution = speed * t - acc * t * t / 2
        xmax = t[np.argmax(move_evolution)]
        ymax = move_evolution.max() 


        comparison_time = [x[0] for x in comparison_data]
        comparison_move = [x[1] for x in comparison_data]
        comparison_speed = [x[2] for x in comparison_data]

        text= "Distance: {:.3f}m - Temps: {:.3f}s".format(xmax, ymax)
        ax = axes[0][0]
        ax.set_title("Everything")
        ax.plot(t, start_speed + acc*t, color="red", label="Speed")
        ax.plot(t,  acc, color="green", label="Acceleration")
        ax.plot(t,  move_evolution, color="blue", label="Move")
        if len(comparison_data) > 0:
            ax.plot(comparison_time, comparison_move, label="Mesure's move")
            ax.plot(comparison_time, comparison_speed, label="Mesure's speed")
        ax.legend()
        ax.annotate(text, xy=(xmax, ymax), xytext=(xmax, ymax-xmax),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

        #axes[0][0].plot(t, np.zeros_like(t), color="black")
        ax = axes[0][1]
        ax.set_title("Position")
        ax.plot(t,  move_evolution, color="blue", label="Position")
        if len(comparison_data) > 0:
            ax.plot(comparison_time, comparison_move, label="Mesure's move")
        ax.legend()

        ax = axes[1][0]
        ax.set_title("Speed")
        ax.plot(t, speed, color="red", label="Speed")
        if len(comparison_data) > 0:
            ax.plot(comparison_time, comparison_speed, label="Mesure's speed")
        ax.legend()
        
        ax = axes[1][1]
        ax.set_title("Acceleration")
        ax.plot(t, acc, color="brown", label="Acceleration")
        ax.legend()


        
        self.__figures.append(fig) 
