import tkinter as tk

class GUI:
    def __init__(self) -> None:
        window = tk.Tk()
        window.maxsize(600,600)
        window.config(bg="black")
        window.title("Caro")
        
        frame = tk.Frame(window,  width=600,  height=  600,  bg='grey')
        frame.grid(row = 0, column = 0)
        
        buttons = []
        for i in range(1,10):
            button = tk.Button(frame, width=20, height=10, bg = "grey", command=clicked)
            buttons.append(button)
            
        row_1 = buttons[0:3]
        row_2 = buttons[3:6]
        row_3 = buttons[6:9]
        
        for button in row_1:
            button.grid(row = 0, column = row_1.index(button))
        for button in row_2:
            button.grid(row = 1, column = row_2.index(button))
        for button in row_3:
            button.grid(row = 2, column = row_3.index(button))
            
        self.window = window
        self.frame = frame
        self.buttons = buttons
        
class Player():
    def __init__(self, name) -> None:
        self.name = name
    
    def play(self, button):
        button.set_text(self.name)
    

if __name__ == "__main__":
    test = GUI()
    x = Player('x')
    y = Player('y')
    test.window.mainloop()