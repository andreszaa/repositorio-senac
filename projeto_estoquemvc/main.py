from tkinter import *
from app.Controller.controller import Controller  # Importa Controller corretamente
from app.View.view import View                    # Importa View corretamente
from app.Model.model import Model                 # Importa Model corretamente

if __name__ == '__main__':
    root = Tk()
    view = View(root)   # Instanciando a View
    model = Model()     # Instanciando o Model
    controller = Controller(model, view)  # Instanciando o Controller
    root.mainloop()
