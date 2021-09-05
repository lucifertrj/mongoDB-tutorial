import pymongo
import tkinter as tk
from tkinter import StringVar, messagebox

def database():
    try:
        #replace username and password into your details
        client = pymongo.MongoClient("mongodb+srv://<username>:<password>@blog.nwryh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client['your_database_name'] #creating a databbse
        #db = client.your_database_name  #other way to create database
        collection = db['your_collection_name']  #create a collection from the database
        return collection  #return database so that functions from button can perform CRUD operation
    except pymongo.errors.ConfigurationError:
        #database can be accessed only if you have active internet connection, this will prompt user the error, if user is not connected to internet
        messagebox.showerror("Network Error","No internet connection")

def insert_db():
    document = dict()
    #get the entered details from the user
    document['name'] = name_entry.get()
    document['mail'] = mail_entry.get()

    #call the database function and get the collection, so that you can perform C-create/insert operation
    collect = database()
    collect.insert_one(document)
    messagebox.showinfo("Sucess","Data Inserted")
    clear()

def delete_db():
    document = dict()
    document['name'] = name_entry.get()
    document['mail'] = mail_entry.get()
    collect = database()

    #call the database function and get the collection, so that you can perform D-delete operation
    collect.delete_one(document)
    messagebox.showinfo("Sucess","Data Deleted")
    clear()

#this function is used to clear the entry box once the data is inserted and deleted
def clear():
    name_entry.delete(0,"end")
    mail_entry.delete(0,"end")
    name_entry.focus_set()

#create a Tkinter GUI application
root = tk.Tk()
root.geometry('430x360+410+200')
root.title("Learn MongoDb")
root.resizable(False,False)

#canvas widget is used to design tkinter GUI, you can add background image, bg color, good scroll bar and etc..
canvas = tk.Canvas(bg="aqua")
canvas.place(x=-1,y=-1,width=460,height=460)

#I suppose this is self-explanary
name = tk.Label(text="Enter your name:",font=("arial",15,"bold")).place(x=10,y=50)
gmail= tk.Label(text="Enter your mail:",font=("arial",15,"bold")).place(x=10,y=110)

name_var = tk.StringVar()
email_var = tk.StringVar()

global name_entry,mail_entry
#get user details to store in database
name_entry = tk.Entry(bd=5,textvariable=name_var,bg="yellow")
name_entry.place(x=180,y=45,width=220,height=45)

mail_entry = tk.Entry(bd=5,textvariable=email_var,bg="yellow")
mail_entry.place(x=180,y=105,width=220,height=45)

#create two buttons for insertion and deletetion operation
insert_btn = tk.Button(bd=4,bg="blue",fg="white",command=insert_db,text="Insert",font=("arial",15,"bold")).place(x=120,y=200)
delete_btn = tk.Button(bd=4,bg="blue",fg="white",command=delete_db,text="Delete",font=("arial",15,"bold")).place(x=250,y=200)

root.mainloop()
"""
you can apply if control conditions to check if the name and email in database exists or not
Go a head and try new stuffs.
Happy coding
"""