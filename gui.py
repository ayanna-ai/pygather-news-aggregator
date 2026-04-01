import tkinter as tk
from tkinter import ttk, messagebox

class NewsGUI:
    def __init__(self, root, fetch_callback):
        self.root = root
        self.root.title("PyGather News Aggregator v1.0")
        self.root.geometry("700x500")
        
        # Header
        self.label = tk.Label(root, text="Global Tech News", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)

        # Table (Treeview)
        self.tree = ttk.Treeview(root, columns=("Source", "Headline", "Time"), show='headings')
        self.tree.heading("Source", text="Source")
        self.tree.heading("Headline", text="Headline")
        self.tree.heading("Time", text="Time")
        self.tree.column("Source", width=100)
        self.tree.column("Headline", width=450)
        self.tree.column("Time", width=80)
        self.tree.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Button
        self.fetch_btn = tk.Button(root, text="Refresh News", command=fetch_callback, 
                                   bg="#007ACC", fg="white", font=("Arial", 10, "bold"))
        self.fetch_btn.pack(pady=20)

    def display_data(self, data_list):
        # Clear old data
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Insert new data
        for item in data_list:
            self.tree.insert("", tk.END, values=(item["Source"], item["Headline"], item["Time"]))