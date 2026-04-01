import tkinter as tk
from gui import DomainApp

def main():
    root = tk.Tk()
    app = DomainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()