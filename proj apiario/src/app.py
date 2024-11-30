import tkinter as tk
#from ui.main_window import MainWindow
from ui.ui_sistema_apiscoop import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()