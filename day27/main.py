import tkinter

window = tkinter.Tk()
window.title("mi primera aplicación en python")
window.minsize(width=500, height=300)


# Creating label

my_label = tkinter.Label(text="I am a label", font = ("Arial", 24, "italic"))
my_label.pack(side="left")












# This code is always at the end
window.mainloop()