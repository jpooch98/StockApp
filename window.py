import tkinter as tk
import matplotlib.pyplot as plt



def show(SP_price, DOW_price):
    # Creates and fromats a window
    window = tk.Tk()
    window.title("Stock Prices")
    message = tk.Label(
        text="The price of the S&P is " + SP_price + "\n The price of the DOW is " + DOW_price,
        width=50,
        height=25)
    message.pack()
    window.mainloop()