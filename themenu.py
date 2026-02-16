import tkinter as tk

root = tk.Tk()

foods = "burger pizza chips burrito"
foods = foods.split()

root.geometry("300x300+1500+400")
root.title("fast food place")

def orderfood():
    selected = listbox.curselection()
    food = listbox.get(selected)
    print(food)
    orderup = tk.Toplevel()
    orderup.title("Your meal")
    tk.Label(orderup, text=f"Heres your {food}").pack()
        


tk.Label(root, text="Big menu:", font=("font", 20)).pack(pady=10)
listbox = tk.Listbox(root, height=10, width=20)
for food in foods:
    listbox.insert(tk.END, food)
listbox.pack(pady=10)
tk.Button(text="Order food", command=orderfood).pack()


root.mainloop()