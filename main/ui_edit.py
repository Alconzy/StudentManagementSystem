from tkinter import ttk

import db
import ui_show


class EditFrame:
    def __init__(self, root, name):
        self.root = root
        self.frame = ttk.Frame(root)
        self.name = name

        # labels
        self.label_name = ttk.Label(self.frame, text='Name')
        self.label_age = ttk.Label(self.frame, text='Age')
        self.label_phone = ttk.Label(self.frame, text='Phone')
        self.label_address = ttk.Label(self.frame, text='Address')

        name, age, phone, address = db.find_by_name(self.name)

        # entry
        self.entry_name = ttk.Label(self.frame, text=name)
        self.entry_age = ttk.Entry(self.frame)
        self.entry_phone = ttk.Entry(self.frame)
        self.entry_address = ttk.Entry(self.frame)

        self.entry_age.insert(0, age)
        self.entry_phone.insert(0, phone)
        self.entry_address.insert(0, address)

        # button
        self.add = ttk.Button(self.frame, text="Add", command=self.do_change)
        self.cancel = ttk.Button(self.frame, text="Cancel", command=self.do_cancel)

        # place
        self.label_name.place(relx=0.025, rely=0.025, height=30, relwidth=0.2)
        self.entry_name.place(relx=0.2, rely=0.025, height=30, relwidth=0.75)

        self.label_age.place(relx=0.025, rely=0.125, height=30, relwidth=0.2)
        self.entry_age.place(relx=0.2, rely=0.125, height=30, relwidth=0.75)

        self.label_phone.place(relx=0.025, rely=0.225, height=30, relwidth=0.2)
        self.entry_phone.place(relx=0.2, rely=0.225, height=30, relwidth=0.75)

        self.label_address.place(relx=0.025, rely=0.325, height=30, relwidth=0.2)
        self.entry_address.place(relx=0.2, rely=0.325, height=30, relwidth=0.75)

        self.cancel.place(relx=0.125, rely=0.425, height=30, relwidth=0.4)
        self.add.place(relx=0.55, rely=0.425, height=30, relwidth=0.4)

        self.frame.place(relx=0, rely=0, relheight=1.0, relwidth=1.0)

    def do_cancel(self):
        self.frame.destroy()
        ui_show.ShowFrame(self.root)

    def do_change(self):
        age = self.entry_age.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()

        db.update(self.name, age, phone, address)

        self.do_cancel()
