import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv

def display_csv_data(file_path):
    try:
        with open('台積電.csv', 'r', newline='') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Read the header row
            tree.delete(*tree.get_children())  # Clear the current data

            tree["columns"] = header
            for col in header:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            for row in csv_reader:
                tree.insert("", "end", values=row)

            status_label.config(text=f"CSV file loaded: {file_path}")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("CSV File Viewer")

tree = ttk.Treeview(root, show="headings")
tree.pack(padx=20, pady=20, fill="both", expand=True)

status_label = tk.Label(root, text="", padx=20, pady=10)
status_label.pack()

root.mainloop()