from tkinter import messagebox
from tkinter import ttk

import db
import ui_add
import ui_edit


class ShowFrame:
    def __init__(self, root):
        self.root = root
        win = ttk.Frame(root)

        # add table
        tree = ttk.Treeview(win, show='headings')
        tree["columns"] = ("Name", "Age", "Phone", "Address")
        tree.column("Name", width=100)
        tree.column("Age", width=100)
        tree.column("Phone", width=100)
        tree.column("Address", width=100)

        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Phone", text="Phone")
        tree.heading("Address", text="Address")

        stu = db.find_all()
        for i, (name, age, phone, address) in enumerate(stu):
            tree.insert("", i, values=(name, age, phone, address))

        tree.place(relx=0.025, rely=0.025, relheight=0.7, relwidth=0.95)

        # add operator
        delete_entry = ttk.Entry(win)
        delete_entry.place(relx=0.025, rely=0.75, height=30, relwidth=0.75)
        btn1 = ttk.Button(win, text="Delete", command=self.delete)
        btn1.place(relx=0.80, rely=0.75, height=30, relwidth=0.175)

        edit_entry = ttk.Entry(win)
        edit_entry.place(relx=0.025, rely=0.82, height=30, relwidth=0.75)
        btn2 = ttk.Button(win, text="Edit", command=self.edit)
        btn2.place(relx=0.80, rely=0.82, height=30, relwidth=0.175)

        btn3 = ttk.Button(win, text="Add new student", command=self.add)
        btn3.place(relx=0.025, rely=0.89, height=30, relwidth=0.95)

        win.place(relx=0, rely=0, relheight=1.0, relwidth=1.0)

        self.frame = win
        self.delete_entry = delete_entry
        self.edit_entry = edit_entry

    def delete(self):
        name = self.delete_entry.get()
        if len(name) == 0:
            return
        result = messagebox.askquestion(title='Warning', message='Delete %s ?' % name)
        if result == 'yes':
            db.delete_by_name(name)
            self.frame.destroy()
            ShowFrame(self.root)

    def edit(self):
        name = self.edit_entry.get()
        if len(name) == 0:
            return
        self.frame.destroy()
        ui_edit.EditFrame(self.root, name)

    def add(self):
        self.frame.destroy()
        ui_add.AddFrame(self.root)
