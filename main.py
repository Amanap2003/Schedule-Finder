import pymongo
import insert
import fetch
import GUI

COLLECTION ='Timetable'
DATABASE = 'PythonProject'


# client=pymongo.MongoClient("mongodb://localhost:27017")
# print(client)
# # DATABASE ='Timetable'
# db=client['PythonProject']
# collection = db['TimeTable']

# basic class info >>
# attributes = {
#     'Lecture' : ''  ,s
#     'Batch': ''     , 
#     'Faculty': ''   , 
#     'Room_No': ''
#     }

# connection with MongoDB
client=pymongo.MongoClient("mongodb://localhost:27017")
print(client)

db=client[DATABASE]
collection = db[COLLECTION]

# print(collection)
# print(type(collection))
# print(type("Hello"))
# print(type(collection.insert_one))
# to insert the data fields in record >> 
# collection.insert_one(attributes)


# db.drop_collection(COLLECTION)

# print("\n\t\n---------------------------------------------------------")
# print("1. Create the database.\n\n2. Show the database\n\n3. Delete the database ")
# print("---------------------------------------------------------")
def ask() :
    print("return to MAIN options ? (y/n) :",end=' ')
    choice=input()
    if choice == 'y' or choice == 'Y' :
        options()
    else :
        print("Exit ? (y/n) :",end=' ')
        choice = input()
        if choice == 'y' or choice =='Y':
            print("\n\t\t\t\t **** EXIT SUCCESSFULLY **** \n\n")
            exit(0)
        else :
            ask() 



def options() :
    print("\n\t\n"+"-"*23+"MAIN"+"-"*28)
    print("\n\t\t1. Create the database.\n\n\t\t2. Show the database\n\n\t\t3. Delete the database\n\n\t\t4. Exit the program :-/\n\t")
    print("-"*27+"-"*28)


    user = input("Enter the choice : ")
    while(user != '0'):
        if (user == '1'):
            db.drop_collection(COLLECTION)

            insert.add_into_db(collection)
            print("\n\t\t\t\t **** DATABASE CREATED **** ")

            ask()
            
        elif (user == '2'):
            fetch.query(COLLECTION)
            fetch.fetch(collection,fetch.exp_and)
            # options()
            ask()
        elif (user == '3'):
            pass
            # db.drop_collection(COLLECTION)
            # print("\n\t\t\t\t **** DATABASE DELETED **** ")
        # user = input("Enter the choice : ")
            # options()
            ask()

        elif(user=='4') :
            print("\n\t\t\t\t **** EXIT SUCCESSFULLY **** \n\n")

            exit(0)
            


# options() 




# insert.add_into_db() 
# fetch.fetch()

if __name__ =="__main__":
    print("hEY !")
    db.drop_collection(COLLECTION)
    insert.add_into_db(collection, GUI.faculty, GUI.batches, GUI.Ltype, GUI.Lcode)
    GUI.run(collection, COLLECTION,db)
    # options() 
    # db.drop_collection(COLLECTION)