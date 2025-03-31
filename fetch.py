# import main
import pandas as pd
from prettytable import PrettyTable
from termcolor import colored
import pymongo


# pd.set_opcclaetion('display.max_rows', None)
# print("1. Filter by Lecture")

# --prototype--
# exp_or={"$or":[{'Batch':"CS34"} , {'Batch':"CS35"}]} 
list_search_or = [{}]

list_search_and=[]
exp_or={"$or":list_search_or} # OR QUERY 
# list_search_and.append(exp_or)

def ask2(collection):
    ch=input("Want to add more filters ? (y/n) : ")
    if (ch=='y' or ch=='Y'):
        query(collection)
    elif (ch=='n' or ch=='N') :
        return
    # the following commmands should not be executed <>
        ch2=input("Want to exit to main ? (y/n) : ")
        if (ch2=='y' or ch2=='Y'):
            return 
        else :
            ask2(collection)
    else :
        print("Enter the valid choice ! \n")
        ask2(collection)

def query(collection) :
    print("\n\t\n"+"-"*23+"SEARCH BY"+"-"*28)
    
    print("\n\t\t1. Enter the Day\n\n\t\t2. Enter the Lecture Type\n\n\t\t3. Enter the lecture code\n\n\t\t4. Enter the Batch\n\n\t\t5. Enter the Faculty\n\n\t\t6. Enter the Room_No\n\n\t\t7. DONE !\n\n\t\t8. Exit to MAIN ?\n\n\t\t")
    print("-"*27+"-"*28)

    user=input("Enter the choice : ")
    if(user == '1'):
        day=input("Enter the day : ")
        list_search_and.append({'Day':day})
        # query(collection)
        # print(list_search_and)

    elif (user == '2'):
        lecturetype=input("Enter the lecture type : ")
        list_search_and.append({'Lecture_Type':lecturetype})
        # query(collection)
    elif (user == '3'):
        lecture=input("Enter the lecture code : ")
        list_search_and.append({'Lecture':lecture})
        # query(collection)
    elif (user == '4'):
        batch=input("Enter the batch : ")
        list_search_and.append({'Batch':batch})
        # query(collection)
    elif (user == '5'):
        faculty=input("Enter the faculty abb. : ")
        list_search_and.append({'Faculty':faculty})
        # query(collection)
    elif (user == '6'):
        Room=input("Enter the room no : ")
        list_search_and.append({'Room_No':Room})
        # query(collection)
    elif(user == '7'):
        fetch(collection,exp_and)
    elif(user == '8'):
        return 
    ask2(collection)
    
     # we have to define the exp_and before calling to fetch function <>
    
exp_and={"$and" : list_search_and} 





# exp_and={"$and" : list_search_and} # AND QUERY









# list_search_or = []
# list_search_or.append({'Batch': "CS34"})
# list_search_or.append({'Batch': "CS35"})
# exp_or={"$or":list_search_or} # OR QUERY 




# list_search_and=[]
# list_search_and.append(exp_or)

# list_search_and.append({'Faculty':"(NTJ)"})





# exp_and={"$and" : list_search_and} # AND QUERY


#  -- prototype for and 
# exp_and={"$and" : [exp_or,{"Faculty":"(NTJ)"}]} # AND QUERY

bold = "\x1b[1m"
underline = "\x1b[4m"
reset = "\x1b[0m"

# exp={"$or":[{'Batch':"A13"},{'Batch':"A17"}]}


def fetch(collection,exp_and):

    listt = collection.find(  exp_and   ,{'_id':0})
    # listt = collection.find(  final_list   ,{'_id':0})
    list_cursor=list(listt)
    # print("Hi")
    # print(list_cursor)
    dataframe=pd.DataFrame(list_cursor)
    
    if(dataframe.empty):
        print("\n\t\n"+"-"*32+" NO LECTURES "+"-"*32)
    else :
        # print("\n\t\n"+"-"*32+"TIME TABLE"+"-"*32+"\n")
        print("\n\n")

        table = PrettyTable()
        table.title = "Time Table"
        table.field_names = list(list_cursor[0].keys())

        for row in list_cursor:
            table.add_row(row.values())
        
        formatted = colored(table,'dark_grey',attrs=['bold'])
        
        # print(f"{bold}{table}{reset}")
        print(formatted)
        # print(dataframe)
        
        
        
        
    # print(exp_and)
# print("HI ")

# fetch=main.collection.find({'Batch': "A13"},{'_id' : 0})
# for rows in fetch :
#     print(rows)
