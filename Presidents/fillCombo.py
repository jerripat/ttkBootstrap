import ttkbootstrap as ttk
from tkinter import *
import tkinter as tk
import sqlite3

root = ttk.Window(tk, themename="superhero")
root.title("Combo Box")
root.geometry("600x500")

def fetch_president_data(selected_president):
    conn = sqlite3.connect("presidents.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Presidents WHERE name=?", (selected_president,))
    data = cursor.fetchone()
    conn.close()
    return data

def on_president_selected(event):
    selected_president = cbo.get()
    data = fetch_president_data(selected_president)
    display_data(data)
    my_label.config(text=f'You Selected {cbo.get()}')

def display_data(data):
    my_listbox.delete(0, tk.END)
    if data:
        my_listbox.insert(tk.END, data)

# Connect to the database
conn = sqlite3.connect("presidents.db")
cursor = conn.cursor()

presidents = []

cursor.execute("SELECT * FROM Presidents")
for pres in cursor.fetchall():
    presidents.append(pres[1])

conn.close()

my_label = ttk.Label(root, text="The Presidents", font=("Arial", 20), foreground="#dbac35")
my_label.pack(pady=30)

cbo = ttk.Combobox(root, font=("Arial", 11), values=presidents, width=20)
cbo.pack(pady=30)

cbo.bind("<<ComboboxSelected>>", on_president_selected)
my_listbox = tk.Listbox(root, width=20, height=5)
for i in range(20):
    my_listbox.insert(tk.END, f"Item {i+1}")
my_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=my_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Attach scrollbar to listbox
my_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
