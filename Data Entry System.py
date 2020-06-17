from tkinter import *

def getvals(): 
   print("Submitting form")
   print(f"{name_value.get(), email_value.get(), ph_value.get(),address_value.get()} ")
   with open("records.txt", "a") as f:
        f.write(f"{name_value.get(), email_value.get(), ph_value.get(),address_value.get()}\n ")

   name_entry.delete(first=0,last=100)
   email_entry.delete(first=0,last=100)
   ph_entry.delete(first=0,last=100)
   address_entry.delete(first=0,last=100)
   name_entry.focus()

root=Tk()
root.title("Data Entry System")
root.geometry("270x180")

#normal form labels 
name=Label(root,text="Name\n")
email=Label(root,text="Email\n")
ph=Label(root,text="Phone no.\n")
address=Label(root,text="Address\n")
name.grid()
email.grid(row=2)
ph.grid(row=4)
address.grid(row=6)

#Entry widget
name_value= StringVar()
email_value= StringVar()
ph_value= StringVar()
address_value=StringVar()

name_entry = Entry(root,textvariable = name_value)
email_entry = Entry(root,textvariable = email_value)
ph_entry = Entry(root,textvariable=ph_value)
address_entry=Entry(root,textvariable=address_value)


name_entry.grid(row=0,column=1)
name_entry.focus()
email_entry.grid(row=2,column=1)
ph_entry.grid(row=4,column=1)
address_entry.grid(row=6,column=1)


#Submit button
Button(text="Submit",command=getvals).grid(column=1)
root.mainloop()