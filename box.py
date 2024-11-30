from tkinter import *
import tkinter.ttk as ttk

from sqlalchemy_utils.types import password

account_list = []

def refresh_table():
    # Clear Table
    for item in table.get_children():
        table.delete(item)

    for account in account_list:
        table.insert("", END, values=account, tags="talabkar" if account[2] >= 0 else "bedehkar")

def reset_form():
    id.set(0)
    name.set("")
    family.set("")
    user.set("")
    password.set("")


    refresh_table()

def save_click():
    account = (id.get(), name.get(), family.get(), user.get(), password.get())
    account_list.append(account)
    reset_form()

def delete_click():
    account = (id.get(), name.get(), family.get(), user.get(), password.get())
    account_list.remove(account)
    reset_form()

def table_select(event):
    # print(event)
    selected_item_id = table.focus()
    # print(selected_item_id)

    selected_item = table.item(selected_item_id)
    account = selected_item["values"]
    id.set(account[0])
    name.set(account[1])
    family.set(account[2])
    user.set(account[3])
    password.set(account[4])

win = Tk()
win.title("My Form")
win.geometry("650x400")

# ID
Label(win, text="ID").place(x=20,y=20)
id = IntVar()
Entry(win ,textvariable=id).place(x=90,y=20)

# Name
Label(win, text="Name").place(x=20,y=60)
name = StringVar()
Entry(win ,textvariable=name).place(x=90,y=60)


# family
Label(win, text="family").place(x=20,y=100)
family = StringVar()
Entry(win ,textvariable=family).place(x=90,y=100)

# user
Label(win, text="user").place(x=20,y=140)
user= StringVar()
Entry(win ,textvariable=user).place(x=90,y=140)

# password
Label(win, text="password").place(x=20,y=180)
password = StringVar()
Entry(win ,textvariable=password).place(x=90,y=180)




table = ttk.Treeview(win, columns=[1, 2, 3,4,5], show="headings")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=140)
table.column(4, width=180)
table.column(5, width=220)

table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="family")
table.heading(4, text="user")
table.heading(5, text="password")

table.tag_configure("bedehkar", background="pink")
table.tag_configure("talabkar", background="lightgreen")

table.place(x=250, y=20)
table.bind("<ButtonRelease>", table_select)
table.bind("<KeyRelease>", table_select)

Button(win, text="Save", command=save_click).place(x=80, y=250)
Button(win, text="Delete", command=delete_click).place(x=150, y=250)



win.mainloop()