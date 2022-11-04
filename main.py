from window import Window
from simulation import Simulation
import tkinter
if __name__ == "__main__":
    window = Window()
    simulation = Simulation()
    window.add_simulation(simulation)
    tkinter.mainloop()
