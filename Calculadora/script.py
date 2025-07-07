import  tkinter as tk
from tkinter import  messagebox
from warnings import catch_warnings

root = tk.Tk()
root.title('calculator')
root.geometry('400x500')
root.resizable(0,0)

colorText = '#000000'
colorButton =  '#e0e0e0'
colorEqualButton = '#4caf50'
colorButtonClear = '#072323'

screenText = tk.StringVar()
screenLabel = tk.Label(root, textvariable=screenText,font=('Arial', 30), bg= '#ffffff', fg=colorText,
                       anchor= 'e', padx=10)
screenLabel.grid(row=0, column=0, columnspan=4, sticky='we', pady=10)

expression = ''

def press(num):
    global expression
    expression += str(num)
    screenText.set(expression)

def equalPess():
    try:
        global expression
        result = str(eval(expression))
        screenText.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Not valid Entry")
        screenText.set('')
        expression = ''

def clear():
    global expression
    screenText.set('')
    expression = ''

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('.',4,0),('0',4,1),('+',4,2)
]

for (text,row,col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial',18),bg=colorButton, fg=colorText,
                       command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

equalButton = tk.Button(root, text='=', width=5, height=2, font=('Arial',18),bg= colorEqualButton, fg='#ffffff', command= equalPess)
equalButton.grid(row=4, column=3, pady=5, padx=5, sticky='nsew')

clearButton = tk.Button(root, text='C', width=5, height=2, font=('Arial',18),bg= colorButtonClear, fg='#ffffff', command= clear)
clearButton.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()