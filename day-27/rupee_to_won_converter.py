import tkinter


window = tkinter.Tk()
window.title("currency converter")
window.geometry("400x300")
window.config(padx=100, pady=100)

#entry
input = tkinter.Entry( width=10)
print(input.get())
input.grid(column=2, row=1)

def rupee_to_won():
    print("converting..")
    new_text = float(input.get()) * 14.23
    calculated_won.config(text=new_text)

#label
rupee = tkinter.Label(window, text="Rupee")
rupee.grid(column=3,row=1)

is_equal_to = tkinter.Label(window, text="is equal to")
is_equal_to.grid(column=1,row=2)

calculated_won = tkinter.Label(window, text="0")
calculated_won.grid(column=2,row=2)

won = tkinter.Label(window, text="won")
won.grid(column=3,row=2)

#button
button = tkinter.Button(window, text="convert",command=rupee_to_won )
button.grid(column=2,row=3)












window.mainloop()
