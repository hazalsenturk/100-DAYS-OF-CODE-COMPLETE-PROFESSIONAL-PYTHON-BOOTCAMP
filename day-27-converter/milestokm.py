from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

km_result_label = Label(text="0")
km_result_label.grid(row=1, column=1)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

def miles_to_km():
    m_input = float(miles_input.get())
    km_result_label.config(text=f"{round(m_input*1.609344,2)}")
    km_result_label.grid(column=1, row=1)


button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)


window.mainloop()
