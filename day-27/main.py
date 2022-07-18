import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label and make it appear

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = tkinter.Entry(width=10)
input.pack()









window.mainloop()