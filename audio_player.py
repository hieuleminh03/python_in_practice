import tkinter as tk

def make_gui():
    pass

class song:
    count = 0
    def __init__(self) -> None:
        count += 1
        self.length = None
        self.author = None
        

if __name__ == "__main__":
    window = tk.Tk()
    label = tk.Label(text="Python rocks!")
    label.pack()

    window.mainloop()
