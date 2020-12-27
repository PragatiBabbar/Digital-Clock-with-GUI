# importing the modules
from time import strftime
from tkinter import Label, Tk

# specifying the window
window = Tk()
window.title("My Digital Clock")
window.geometry("200x140")
window.config(bg="aqua")
window.resizable(True, True)

# specifying the time appearance
clock_label = Label(window, bg="black", fg="white", font=("Arial", 15, 'bold'), relief='flat')
clock_label.place(x=20, y=20)


# function to get the current time
def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.config(text=current_time)
    clock_label.after(80, update_label)


# calling the function
update_label()
window.mainloop()
