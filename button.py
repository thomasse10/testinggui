import tkinter as tk
import random


root = tk.Tk()
image = tk.PhotoImage(file="hello.gif")

def hi_func():
    for i in range(3):
        window = tk.Toplevel(root)
        window.geometry(f"200x180+{random.randint(40,1900)}+{random.randint(40,900)}")
        hi_pic = tk.Label(window, image=image)
        hi_pic.pack()
        tk.Label(window, text="Hi there",).pack()

root.geometry("400x400+1700+400")

hi = tk.Button(root, text="hi", command=hi_func,)
hi2 = tk.Button(root, image=image, command=hi_func,)
hi.pack()
hi2.pack()

root.mainloop()