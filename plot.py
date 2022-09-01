from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Plot")
root.iconbitmap()
root.geometry("400x200")
root.resizable(False, False)

def graph():
    car_prices = np.random.normal(200000, 2500, 5000)
    plt.hist(car_prices, bins=50, color='r')
    plt.show()


button = Button(root, text = "View Graph", command= graph)
button.pack()

root.mainloop()