from window import Window
from simulation import Simulation
import tkinter
if __name__ == "__main__":
    window = Window()
    simulation = Simulation(k=0, e=5, m=0.200)
    window.add_simulation(simulation)
    tkinter.mainloop()