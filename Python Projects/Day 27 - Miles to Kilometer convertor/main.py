from tkinter import *

window = Tk()
window.title("Miles to Kilometer convertor")
window.config(padx=20,pady=20)

miles_input = Entry()
miles_input.grid(row=0,column=1)
miles_label = Label(text="Miles")
miles_label.grid(row=0,column=2)

is_equal_to_label = Label(text="is_equal to")
is_equal_to_label.grid(row=1,column=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1,column=1)
kilometer_label = Label(text="Km")
kilometer_label.grid(row=1,column=2)

def calculate_km():
    value = float(miles_input.get())
    km_value = value * 1.609
    kilometer_result_label.config(text=km_value)


calculate = Button(text="Calculate",command=calculate_km)
calculate.grid(row=2,column=1)





window.mainloop()