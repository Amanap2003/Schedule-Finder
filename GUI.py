from tkinter import *  
from ttkthemes import ThemedTk 
from ttkthemes import * 


import fetch

batches = set([""])
faculty= set([""])
Ltype = set([""])
Day = set(["MON", "TUE","WED", "THU", "FRI", "SAT", ""])
Lcode = set([""])



def run(collection, COLLECTION, db) :
    
    root = Tk()
    # root = ThemedTk(theme="black")
    root.geometry("550x300")
    # style = ttk.Style()
    # style.theme_use("classic")
    
    root.title("Get TimeTable")

   
    # root.config(bg='#002b36')
    # ------------------------------------------------

    Batch_select= StringVar()
    Faculty_select = StringVar()
    Ltype_select = StringVar()
    Lcode_select = StringVar()
    Day_select = StringVar()

    # batches = ["CS34","CS35","CS37","CS38","ALL"]
    # faculty = ["NTJ","SWT","PKR","EMP","MTS"]
   
    # Lcode = ["1212","1212","1212","1212"]
    # Ltype = ["L","P"]
    # Day = ["Mon","TUE","WED","THU","FRI","SAT"]
    Batch_select.set("CS34")
    Faculty_select.set("(NTJ)") 
    Ltype_select.set("P")
    Lcode_select.set("")
    Day_select.set("MON")

    
    list_updating=[]


    Batch_Menu = OptionMenu(root , Batch_select, *batches)
    Faculty_Menu = OptionMenu(root , Faculty_select, *faculty)
    Ltype_Menu = OptionMenu(root ,Ltype_select, *Ltype)
    Lcode_Menu = OptionMenu(root , Lcode_select, *Lcode)
    Day_Menu = OptionMenu(root , Day_select, *Day)


    def closed():
        db.drop_collection(COLLECTION)
        print("\n\t\t\t\t **** EXIT SUCCESSFULLY **** \n\n")
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", closed)

    def done():
        try :
            if(len(Batch_select.get()) != 0):
                list_updating.append({'Batch' : Batch_select.get()})
            if(len(Faculty_select.get()) != 0):
                list_updating.append({'Faculty':Faculty_select.get()})
            if(len(Day_select.get()) != 0 ):
                list_updating.append({'Day':Day_select.get()})
            if(len(Ltype_select.get())!= 0):
                list_updating.append({'Lecture_Type':Ltype_select.get()})
            if(len(Lcode_select.get()) != 0):
                list_updating.append({'Lecture':Lcode_select.get()})
            
            
            final_list = { "$and" : list_updating }
            # list_search_or = [{}]
            # exp_or={"$or":list_search_or}
            # list_updating.append(exp_or)
            # print(list_updating)
            fetch.fetch(collection,final_list)
            final_list = { "$and" : list_updating }
            list_updating.clear()

        except Exception as e :
            print(f'Error : {e}')
        
        # print(final_list)
        # demo.config(text =  ', '.join(final_list))
        # demo.grid(row=6,column=0)

        
    

    def reset():
        Batch_select.set("CS34")
        Faculty_select.set("(NTJ)")
        Ltype_select.set("P")
        Lcode_select.set("")
        Day_select.set("MON")
     
        list_updating.clear()
        
    

    Submit = Button(root,text=" Show ",  width=20, command=done)
    Reset = Button(root,text=" Reset ",  width=20, command=reset)





    Batch_Label = Label(root, text="Select the batch : ", font=('Courier',12))
    Faculty_Label = Label(root, text="Select the Faculty : ", font=('Courier',12))
    Ltype_Label = Label(root, text="Select the Lecture Type : ", font=('Courier',12))
    Lcode_Label = Label(root, text="Select the Lecture Code : ", font=('Courier',12))
    Day_Label = Label(root, text="Select the Day  : ", font=('Courier',12))

    demo = Label(root , text = "")




    Batch_Menu.grid(row = 0 ,column=1,padx=10,pady=10)
    Faculty_Menu.grid(row = 1 ,column=1,padx=10,pady=10)
    Ltype_Menu.grid(row = 2 ,column=1,padx=10,pady=10)
    Lcode_Menu.grid(row = 3 ,column=1,padx=10,pady=10)
    Day_Menu.grid(row = 4 ,column=1,padx=10,pady=10)

    Submit.grid(row=5, column=0, padx=15, pady=15)
    Reset.grid(row=5, column=1, padx=15, pady=15)

    # Labels places 
    Batch_Label.grid(row = 0, column=0, padx=10, pady=10)
    Faculty_Label.grid(row = 1, column=0, padx=10, pady=10)
    Ltype_Label.grid(row = 2, column=0, padx=10, pady=10)
    Lcode_Label.grid(row = 3, column=0, padx=10, pady=10)
    Day_Label.grid(row = 4, column=0, padx=10, pady=10)
    # -----------------------------------------------------
    root.mainloop()













# -----------------------------------------------
