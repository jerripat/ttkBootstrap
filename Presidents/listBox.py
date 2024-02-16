import sqlite3
import tkinter as tk
root = tk.Tk()
root.title("Listbox Example")
root.geometry("500x300")
root.configure(background="#dbac35")

def fillListbox():

    conn = sqlite3.connect('presidents.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Presidents")
    data = cursor.fetchmany()


    # Create a Listbox widget
    listbox = tk.Listbox(root, width=400,font=("Arial", 14))
    listbox.pack(padx=10, pady=10)

    # Add data to the Listbox
    for item in data:

        listbox.insert(tk.END, ' '.join(str(i) for i in data))

fillListbox()
root.mainloop()
