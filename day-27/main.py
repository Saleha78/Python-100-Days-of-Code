import tkinter

window = tkinter.Tk()
window.title("My first window")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

#label
my_label = tkinter.Label(window, text="I am a Label", font=("Arial", 25,"bold"))
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)

#to make changes on the already created label
my_label["text"] = "I am another Label"
my_label.config(font=("Arial", 20))

#button

def button_clicked():
    print ("I am clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(window, text="Click me",command=button_clicked ) #command=button_clicked     # Give the function
button.grid(column=2,row=2)                                                           #command=button_clicked()   # Run the function immediately

                                                                         # that is why we are not using parenthesis if still
                                                                         # has doubt run the program with parenthesis
new_button = tkinter.Button(window, text="Click me",command=button_clicked ) #command=button_clicked     # Give the function
new_button.grid(column=3,row=1)

#entry
input = tkinter.Entry( width=10)
print(input.get())
input.grid(column=5, row=5)







window.mainloop()