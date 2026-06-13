import tkinter as tk
from tkinter import ttk, messagebox

class StudentView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎓 Student Information System")
        self.geometry("850x500")
        self.configure(padx=15, pady=15)
        
        self.on_add_click = None
        self.on_delete_click = None
        self.on_update_click = None
        self.on_stats_click = None
        self.on_select_record = None

        self.create_layout()

    def create_layout(self):
        form_frame = ttk.LabelFrame(self, text=" Student Records Engine ", padding=15)
        form_frame.pack(side=tk.LEFT, fill=tk.Y, expand=False, padx=(0, 15))

        ttk.Label(form_frame, text="Student ID:").pack(anchor=tk.W, pady=(0, 2))
        self.ent_id = ttk.Entry(form_frame, width=25)
        self.ent_id.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(form_frame, text="Full Name:").pack(anchor=tk.W, pady=(0, 2))
        self.ent_name = ttk.Entry(form_frame, width=25)
        self.ent_name.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(form_frame, text="Age:").pack(anchor=tk.W, pady=(0, 2))
        self.ent_age = ttk.Entry(form_frame, width=25)
        self.ent_age.pack(fill=tk.X, pady=(0, 15))

        self.btn_add = ttk.Button(form_frame, text="➕ Register Student", command=lambda: self.on_add_click())
        self.btn_add.pack(fill=tk.X, pady=3)

        self.btn_update = ttk.Button(form_frame, text="✏️ Update Selected", command=lambda: self.on_update_click())
        self.btn_update.pack(fill=tk.X, pady=3)

        self.btn_delete = ttk.Button(form_frame, text="🗑️ Delete Selected", command=lambda: self.on_delete_click())
        self.btn_delete.pack(fill=tk.X, pady=3)

        self.btn_stats = ttk.Button(form_frame, text="📊 System Statistics", command=lambda: self.on_stats_click())
        self.btn_stats.pack(fill=tk.X, pady=(15, 0))

        table_frame = ttk.Frame(self)
        table_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        scroll = ttk.Scrollbar(table_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree = ttk.Treeview(table_frame, columns=("ID", "Name", "Age"), show="headings", yscrollcommand=scroll.set)
        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Full Name")
        self.tree.heading("Age", text="Age")
        
        self.tree.column("ID", width=100, anchor=tk.CENTER)
        self.tree.column("Name", width=250, anchor=tk.W)
        self.tree.column("Age", width=80, anchor=tk.CENTER)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        scroll.config(command=self.tree.yview)

        self.tree.bind("<<TreeviewSelect>>", lambda event: self.on_select_record())

    def get_inputs(self):
        return self.ent_id.get().strip(), self.ent_name.get().strip(), self.ent_age.get().strip()

    def set_inputs(self, sid, name, age):
        self.clear_inputs()
        self.ent_id.insert(0, sid)
        self.ent_name.insert(0, name)
        self.ent_age.insert(0, age)

    def clear_inputs(self):
        self.ent_id.delete(0, tk.END)
        self.ent_name.delete(0, tk.END)
        self.ent_age.delete(0, tk.END)

    def refresh_directory(self, students):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for s in students:
            self.tree.insert("", tk.END, values=(s.id, s.name, s.age))

    def show_message(self, title, message, is_error=False):
        if is_error:
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)