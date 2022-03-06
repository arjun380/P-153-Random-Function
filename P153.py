from tkinter import *
import random

root=Tk()
root.title("Testing with random function")
root.geometry("400x400")

txt_inp = Entry(root)
label = Label(root)
gen_passw = Label(root)

array_3d = [[[7,8,9,0,1,2],["King","Queen"],["I","J","K","L","M","N","O","P"]]]
print(array_3d[0][2][3])

def new_password():
    label["text"] = "Guessed Password: " + txt_inp.get()
    
    random_no_1 = random.randint(0,5)
    
    random_no_2 = random.randint(0,1)
    
    random_no_3 = random.randint(0,7)
    
    letter_1 = str(array_3d[0][0][random_no_1])
    
    letter_2 = (array_3d[0][1][random_no_2])
    
    letter_3 = (array_3d[0][2][random_no_3])
    gen_passw["text"] = letter_1 + "" +letter_2 + "" + letter_3
    




    
btn = Button(root, text="Generate Password", command = new_password)

txt_inp.place(relx = 0.5, rely = 0.3, anchor = CENTER)

label.place(relx = 0.5, rely = 0.4, anchor = CENTER)


btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

gen_passw.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()