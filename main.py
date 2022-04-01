#import libraries

import tkinter as tk
from functools import partial

def call_solution(show_solution, num_1, num_2):  
    number_1 = (num_1.get())
    number_2 = (num_2.get())
    solution = float(number_1) + float(number_2)
    show_solution.config(text="Result = %d" % solution)  
    return  
   
root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="A", ).grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="B", ).grid(row=2, column=0)  
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
call_solution = partial(call_solution, labelResult, number1, number2)  
  
buttonCal = tk.Button(root, text="Calculate", command=call_solution).grid(row=3, column=0)  
  
root.mainloop()  