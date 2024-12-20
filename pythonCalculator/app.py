import tkinter as tk 

calculation = ""
def appendToDisplay(symbol) :
    global calculation
    calculation += str(symbol)
    displayResult.delete(1.0,"end")
    displayResult.insert(1.0, calculation)

def calculate():
    global calculation
    try:
        calculation = str(eval(calculation))
        displayResult.delete(1.0, "end")
        displayResult.insert(1.0, calculation)
    except:
        clearDisplay()
        displayResult.insert(1.0, "Error")
    finally:
        calculation = ""

def clearDisplay() :
    global calculation
    calculation = ""
    displayResult.delete(1.0 , "end")



display = tk.Tk()
display.geometry("400x375")

displayResult = tk.Text(display, height=2 ,width=16,font=("Arial", 24))
displayResult.grid(columnspan=5)

#Numbers
button1 = tk.Button(display, text="1" , command=lambda: appendToDisplay(1), width=5 , font=("Arial" , 14))
button1.grid(row=2 , column=1)

button2 = tk.Button(display, text="2" , command=lambda: appendToDisplay(2), width=5 , font=("Arial" , 14))
button2.grid(row=2 , column=2)

button3 = tk.Button(display, text="3" , command=lambda: appendToDisplay(3), width=5 , font=("Arial" , 14))
button3.grid(row=2 , column=3)

button4 = tk.Button(display, text="4" , command=lambda: appendToDisplay(4), width=5 , font=("Arial" , 14))
button4.grid(row=3 , column=1)

button5 = tk.Button(display, text="5" , command=lambda: appendToDisplay(5), width=5 , font=("Arial" , 14))
button5.grid(row=3 , column=2)

button6 = tk.Button(display, text="6" , command=lambda: appendToDisplay(6) ,width=5 , font=("Arial" , 14))
button6.grid(row=3 , column=3)

button7 = tk.Button(display, text="7" , command=lambda: appendToDisplay(7), width=5 , font=("Arial" , 14))
button7.grid(row=4 , column=1)

button8 = tk.Button(display, text="8" , command=lambda: appendToDisplay(8), width=5 , font=("Arial" , 14))
button8.grid(row=4 , column=2)

button9 = tk.Button(display, text="9" , command=lambda: appendToDisplay(9), width=5 , font=("Arial" , 14))
button9.grid(row=4 , column=3)

button0 = tk.Button(display, text="0" , command=lambda: appendToDisplay(0), width=5 , font=("Arial" , 14))
button0.grid(row=5 , column=2)

#Operators
button_plus = tk.Button(display, text="+" , command=lambda: appendToDisplay("+"), width=5 , font=("Arial" , 14))
button_plus.grid(row=2 , column=4)

button_minus = tk.Button(display, text="-" , command=lambda: appendToDisplay("-"), width=5 , font=("Arial" , 14))
button_minus.grid(row=3 , column=4)

button_multiply = tk.Button(display, text="*" , command=lambda: appendToDisplay("*"), width=5 , font=("Arial" , 14))
button_multiply.grid(row=4 , column=4)

button_divide = tk.Button(display, text="/" , command=lambda: appendToDisplay("/"), width=5 , font=("Arial" , 14))
button_divide.grid(row=5 , column=4)

button_open = tk.Button(display, text="(" , command=lambda: appendToDisplay("("), width=5 , font=("Arial" , 14))
button_open.grid(row=5 , column=1)

button_close = tk.Button(display, text=")" , command=lambda: appendToDisplay(")"), width=5 , font=("Arial" , 14))
button_close.grid(row=5 , column=3)

button_clear = tk.Button(display, text="C" , command=clearDisplay, width=11 , font=("Arial" , 14))
button_clear.grid(row=6 , column=1 ,columnspan=2)

button_equal = tk.Button(display, text="=" , command=calculate, width=11 , font=("Arial" , 14))
button_equal.grid(row=6 , column=3 , columnspan=2)

display.mainloop()