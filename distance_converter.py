from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)
MY_FONT = ("Arial", 15, "normal")


# Converter function
def converter():
    option = radio_state.get()
    try:
        value = float(input.get())
        if option ==1:
            km = round(value *1.609344)
        else:
            km = round(value * 1760)
        ans_label.config(text= km)
        msg_label.config(text= "")
    except ValueError:
        msg_label.config(text= "Invalid input. Please enter a valid number.", fg="red")


# Option label button

option_label = Label(text= "Choose Option", font = ("Arial", 15, "bold"))
option_label.grid(row=0, column=1)
option_label.config(pady=20)

# radio button
def radio_selected():
    selection = radio_state.get()
    if selection != 1:
        km_label.config(text= "yard")
    else:
        km_label.config(text= "Km")


radio_state = IntVar()
radio_state.set(1)
radio1 = Radiobutton(text= "Miles to Km", value= 1, variable= radio_state, command=radio_selected)
radio1.grid(row=1, column=0)
radio1.config(pady=15)
radio2 = Radiobutton(text= "Miles to yard", value= 2, variable= radio_state, command=radio_selected)
radio2.grid(row=1, column=2)
radio2.config(pady=15)

# Input area

input = Entry(width=10, borderwidth=2, border= 5)
input.grid(row=2, column=1)

# label-1 for "Miles"
miles_label = Label(text= "Miles", font = MY_FONT)
miles_label.grid(row=2, column=2)
miles_label.config(padx=10)

# label-2 for "is equal to"

label2 = Label(text="is equal to ", font= MY_FONT)
label2.grid(row=3, column=0)
label2.config(pady=10)

# Answer label by default 0

ans_label = Label(text= 0, font= MY_FONT, border= 3)
ans_label.grid(row=3, column=1)
ans_label.config(pady=20,padx=20)

# Kilometer label "Km"

km_label = Label(text= "Km", font= MY_FONT)
km_label.grid(row=3, column=2)
km_label.config(pady=10,padx=20)

# Message label

msg_label = Label(font= MY_FONT)
msg_label.grid(row=5, column=1, columnspan= 2 , sticky= "w")
msg_label.config(pady=10,padx=20)


# Calculate button
button = Button(text= "Calculate", font= MY_FONT, activebackground="Blue", command= converter)
button.grid(row=4, column=1)



window.mainloop()