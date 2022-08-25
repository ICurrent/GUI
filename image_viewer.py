from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.resizable(False, False)

#create functionality
def next(image_number):
    global label, butt_next, butt_prev
    label.grid_forget()
    label = Label(image=image_list[image_number - 1])
    butt_next = Button(root, text = "Next", command=lambda: next(image_number+1))
    butt_prev = Button(root, text = "Prev", command=lambda: prev(image_number-1))
    label.grid(row=0, column=0, columnspan=3)

    if image_number == 3:
        butt_next =  Button(root, text = "Next", state=DISABLED)
    butt_next.grid(row=1, column=2)
    butt_prev.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " 0f " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def prev(image_number):
    global label, butt_next, butt_prev
    label.grid_forget()
    label = Label(image=image_list[image_number - 1])
    butt_next = Button(root, text = "Next", command=lambda: next(image_number+1))
    butt_prev = Button(root, text = "Prev", command=lambda: prev(image_number-1))
    label.grid(row=0, column=0, columnspan=3)

    if image_number == 1:
        butt_prev = Button(root, text = "Prev", state=DISABLED)
    butt_next.grid(row=1, column=2)
    butt_prev.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " 0f " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

img_1 = ImageTk.PhotoImage(Image.open("image/images.jpg"))
img_2 = ImageTk.PhotoImage(Image.open("image/images.png"))
img_3 = ImageTk.PhotoImage(Image.open("image/images.jpg"))
# img_4 = ImageTk.PhotoImage(Image.open("image/code.png"))
# img_5 = ImageTk.PhotoImage(Image.open("image/images.png"))

image_list = [img_1, img_2, img_3]

status = Label(root, text="Image 1 0f " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

label = Label(image=img_1)
label.grid(row=0, column=0, columnspan=3)



butt_next = Button(root, text = "Next", command=lambda: next(2))
butt_next.grid(row=1, column=2, pady=10)

butt_prev = Button(root, text = "Prev", command=prev, state=DISABLED)
butt_prev.grid(row=1, column=0)

butt_exit = Button(root, text = "Exit Program", command=root.quit)
butt_exit.grid(row=1, column=1)


root.mainloop()