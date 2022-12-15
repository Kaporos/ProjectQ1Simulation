from matplotlib import numpy
import matplotlib.pyplot as plt
import numpy as np
import math

class Simulation:
    def __init__(self):
        """
        Simulation variables
        """
        self.mu_c = 0.04 # Constante frottements sol modele constant
        self.klin = 0.04 # Constante frottements sol modele linéaire
        #self.rig = 20 # Constante rigidité élastique
        self.m = 0.250 # Masse du véhicule [Kilos]
        self.dt = 0.01 # Timestep [Seconds]
        #self.x = 0.60 # Etirement elastique [Metres]
        self.v0 = 7 # Vitesse initiale du véhicule [m/s]
        self.comparisonOffset = 1.200123E0 # Décalage entre les données mesurées via tracker et la simulation
        self.__figures = []
    def figures(self):
        return self.__figures
    
    def graph(self, comparison_data):
        self.__figures = []

        fig, axes = plt.subplots(2,2, constrained_layout=True)  # 4 graphes 
        """
        Modele Constant (MRUA)
        """
        t = np.arange(0, 1000, self.dt) #  Time Array [0,0.01,0.02,0.03,....3]
        acc = np.full_like(t, -1*self.mu_c*9.81) # acc = -kg
        start_speed = np.full_like(t, self.v0) # start_speed = v0
        speed = start_speed + acc * t 
        move_evolution = speed * t - acc * t * t / 2

        ymax = move_evolution.max() #Déplacement maximal pour la légende
        xmax = t[np.argmax(move_evolution[:len(t)])]

        """
        Modele Lineaire
        """
        speed_lin = []
        for a in t: 
            speed_lin.append(self.v0 * math.pow(math.e, (-1*self.klin*a)/self.m))
        speed_lin = np.array(speed_lin)
        move_lin = (self.m/self.klin)*self.v0 - (self.m/self.klin)*speed_lin

        xlinmax = t[np.argmax(move_lin)] #Déplacement maximal pour la légende
        ylinmax = move_lin.max() 


        """
        Stop the graph when speed = 0 (on the constant simulation)
        """
        last_speed_const = np.where(speed < 0.25 )[0][0]
        last_speed_lin = np.where(speed_lin < 0.25 )[0][0]
        t_lin = t.copy()
        t = t[:last_speed_const]
        t_lin = t_lin[:last_speed_lin]

        """
        Retrieving comparison data from the tracker
        """
        comparison_time = np.array([x[0] for x in comparison_data]) - self.comparisonOffset
        comparison_move = [x[1] for x in comparison_data]
        comparison_speed = [x[2] for x in comparison_data]

        """
        Plotting
        """
        text= "Distance: {:.3f}m - Temps: {:.3f}s".format(ymax, xmax)
        ax = axes[0][0]
        ax.margins(x=0.01)
        ax.set_title("Position - Modele Constant")
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Position [m]")
        ax.plot(t,  move_evolution[:len(t)], color="blue", label="Position")
        if len(comparison_data) > 0:
            ax.plot(comparison_time, comparison_move, label="Mesure's move")
        ax.legend()
        ax.annotate(text, xy=(0,0))

        ax = axes[1][0]
        ax.margins(x=0.01)
        ax.set_title("Speed - Modele Constant")
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Speed [m/s]")
        ax.plot(t, speed[:len(t)], color="red", label="Speed")
        if len(comparison_data) > 0:
            ax.plot(comparison_time, comparison_speed, label="Mesure's speed")
        ax.legend()

        
        text= "Distance: {:.3f}m - Temps: {:.3f}s".format(ylinmax, xlinmax)
        ax = axes[0][1]
        ax.margins(x=0.01)
        ax.set_title("Position - Modele Lineaire")
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Position [m]")
        ax.plot(t_lin, move_lin[:len(t_lin)], color="green", label="Position")
        if len(comparison_data) > 0:
            ax.plot(comparison_time, comparison_move, label="Mesure's speed")
        ax.legend()
        ax.annotate(text, xy=(0,move_lin[-1]), xytext=(0, move_lin[-1]+move_lin[-1]/15))
        ax.annotate(text, xy=(0,0))

        ax = axes[1][1]
        ax.margins(x=0.01)
        ax.set_title("Speed - Modele Lineaire")
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Speed [m/s]")
        ax.plot(t_lin, speed_lin[:len(t_lin)], color="orange", label="Speed")
        if len(comparison_data) > 0:
            ax.plot(comparison_time, comparison_speed, label="Mesure's speed")
        ax.legend()
        
        self.__figures.append(fig) 
