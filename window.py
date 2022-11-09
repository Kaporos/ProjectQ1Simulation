import tkinter
from tkinter import filedialog as fd
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)

class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.wm_title("Simulation physique")
        self.buttonZone = tkinter.Frame(self.root)
        self.loadFileBtn = tkinter.Button(self.buttonZone, text="Load File", command=lambda: self.load_file())
        self.loadFileBtn.grid(row=0, column=0)
        self.comparaison_data = []
        self.simulation = None
    def load_file(self):
        filename = fd.askopenfilename()
        self.comparaison_data = []
        with open(filename) as f:
            lines = [x.split(" ") for x in f.readlines()]
            for i in lines:
                if len(i) != 3:
                    continue
                try:
                    self.comparaison_data.append([float(x) for x in i])
                except:
                    print("Invalid data")
                    self.comparaison_data = []
                    break
        self.draw_simulation(self.simulation)

    def add_simulation(self, simulation):
        params = [x for x in dir(simulation) if (not x.startswith("_")) and type(getattr(simulation, x)) != type(self.add_simulation)]
        #b=tkinter.Frame(self.root,border=5)
        b = self.buttonZone
        paramsEntries = {}
        for (index,param) in enumerate(params):
            value = getattr(simulation, param)
            tkinter.Label(b, text=param).grid(row=index+1)
            e1 = tkinter.Entry(b)
            e1.insert(0, str(value))
            e1.grid(row=index+1, column=1)
            paramsEntries[param] = e1
        simulation.paramsEntries = paramsEntries
        update = tkinter.Button(b, text="Update", command=lambda : self.update_simulation_params(simulation))
        update.grid(row=len(params)+1)
        b.pack()
        simulation.canvases = []
        self.simulation = simulation
        self.draw_simulation(simulation)
    def update_simulation_params(self, simulation):
        for param in simulation.paramsEntries.keys():
            value = simulation.paramsEntries[param].get()
            setattr(simulation, param, float(value))
        self.draw_simulation(simulation)
    def draw_simulation(self, simulation):
        simulation.graph(self.comparaison_data)
        for canvas in simulation.canvases:
            canvas.get_tk_widget().destroy()
        simulation.canvases = []
        for figure in simulation.figures():
            canvas = FigureCanvasTkAgg(figure, master=self.root)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
            simulation.canvases.append(canvas)
