import tkinter as tk

root = tk.Tk()
root.title("window title test")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("400x400+1150+500")
tk.Label(root, text="hello").pack()
tk.Label(root, text="there").pack()
image = tk.PhotoImage(file="image.png")
tk.Label(root, image=image).pack()
root.mainloop()