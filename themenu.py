import tkinter as tk

root = tk.Tk()

foods = "burger pizza fries burrito"
foods = foods.split()
images = {
    "burger": tk.PhotoImage(file="burger.png"),
    "pizza": tk.PhotoImage(file="pizza.png"),
    "fries": tk.PhotoImage(file="fries.png"),
    "burrito": tk.PhotoImage(file="burrito.png")
}


root.geometry("300x300+1500+400")
root.title("fast food place")

def orderfood():
    selected = listbox.curselection()
    if not selected:
        return None
    food = listbox.get(selected)
    print(food)
    orderup = tk.Toplevel()
    orderup.title("Your meal")
    img = images[food]
    tk.Label(orderup, image=img).pack()
    tk.Label(orderup, text=f"Heres your {food}", font=("font",20)).pack(pady=10)
        


tk.Label(root, text="Pick a food:", font=("font", 20)).pack(pady=10)
listbox = tk.Listbox(root, height=10, width=20)
for food in foods:
    listbox.insert(tk.END, food)
listbox.pack(pady=10)
tk.Button(text="Order food", command=orderfood).pack()


root.mainloop()