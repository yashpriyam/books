from tkinter import *
import backend  #we are importing the other python file in which we have created backend part

def view_command():
    list1.delete(0,END) #so that you dont add same list to the database everytime you press view all
    for row in backend.view():
        list1.insert(END,row) #put the number within the bracket at which position you want to put your entry in the list1
                                ##or END,row if you want every new entry in a new line after the previous entry
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):  # since the search command has parameters, user can type in any one of the parameters and would want entries with that one parameter
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)     #this ensures that the list is always empty before any new Entry
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))        #so that we can see the new entry just there in the list box

def get_selected_row(event):
    try:      #when we use the bind function '<<>>' with a function, python expects an 'event'
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        #return(selected_tuple)
        e1.delete(0,END)        #when you select a row alll the entries of the row are displayed in the respective boxes
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:          #this line prevents error when you click on empty list box in your window
        pass
def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    #print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])

window=Tk()

window.wm_title("BOOKstore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)


l3=Label(window,text="Year")
l3.grid(row=1,column=0)


l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)


sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)    #<<>>is the bind function

b1=Button(window,text="View all",width=12,command=view_command) #to execute a function when athe button is pressed
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)
window.mainloop()

#pyinstaller helps you create a standalone executable file of your program
#pyinstaller --onefile --windowed book.py
