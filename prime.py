import tkinter as tk
import requests as rq
import json

# xu ly
def process():
    input = entry.get()
    if check_input(input):
        link = 'https://prime-number-api.onrender.com/checkIfPrime?num=' + str(input)
        response = rq.get(link)
        content = response.content.decode('utf-8')
        data = json.loads(content)[0][str(input)]
        if data:
            result_label.config(text=str(input) + ' is a prime number')
            result_label.pack(pady=10)
        else:
            result_label.config(text=str(input) + ' is not a prime number')
            result_label.pack(pady=10)
    else:
        result_label.config(text='Input not valid')
        result_label.pack(pady=10)
    
def check_input(input):
    try:
        int(input)
        return 1
    except ValueError:
        return 0
    
def on_enter_press(event):
    process()

# giao dien
window = tk.Tk()
window.title('Check Prime')
window.configure(background='#333333')
window.minsize(600,200)
window.resizable(False, False)
window.bind('<Return>', on_enter_press)

# element
label = tk.Label(text='Enter a number:')
label.pack(pady=15)

entry = tk.Entry(width=50)
entry.pack(pady=10)

button = tk.Button(text='Check', command=process)
button.pack(pady=10)

result_label = tk.Label()

window.mainloop()