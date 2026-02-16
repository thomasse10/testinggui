import tkinter as tk

root = tk.Tk()

foods = "burger pizza chips burrito"
foods = foods.split()

root.geometry("300x300+1500+400")

tk.Label(root, text="Big menu:", font=("font", 20)).pack(pady=10)
listbox = tk.Listbox(root, height=30, width=20)
for food in foods:
    listbox.insert(tk.END, food)
listbox.pack(pady=10)



root.mainloop()