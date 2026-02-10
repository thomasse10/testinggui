import tkinter as tk

root = tk.Tk()
tk.Label(root, text="Heres some text").pack()
root.geometry("500x500+1150+450")
image = tk.PhotoImage(file="image.png")
tk.Label(root, image=image).pack()

root.mainloop()