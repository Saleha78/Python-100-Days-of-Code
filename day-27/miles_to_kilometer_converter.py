import tkinter

window = tkinter.Tk()
window.title("Miles to km converter")
window.geometry("400x200")
window.configure(padx=100, pady=30)

#label
label_1 = tkinter.Label(window, text="is equal to")
label_1.grid(column=1, row=2)
label_1.config(font=("Arial", 15))

label_2 = tkinter.Label(window, text="km")
label_2.grid(column=3, row=2)
label_2.config(font=("Arial", 15))

label_3 = tkinter.Label(window, text="0")
label_3.grid(column=2, row=2)
label_3.config(font=("Arial", 10))

label_4 = tkinter.Label(window, text="Miles")
label_4.grid(column=3, row=1)
label_4.config(font=("Arial", 15))


#button
def miles_to_km():
    print ("Calculating...")
    new_text = float(input.get()) * 1.60934
    label_3.config(text=new_text)

#button
button = tkinter.Button(window, text="Calculate", command=miles_to_km) #command=button_clicked     # Give the function
button.grid(column=2,row=3)
button.config(font=("Arial", 10))


#entry
input = tkinter.Entry( width=10)
print(input.get())
input.grid(column=2, row=1)










window.mainloop()