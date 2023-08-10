print("_"*40)
print("                                       ")
print("*******STUDENT MANAGEMENT SYSTEM*******")
print("_"*40)

l=["Deepak","Nikhil","Tannu","Kaku"]

def open_list():
    for i in range(len(l)):
                   print(l[i])

def add_list():
    a=input("Enter Name to add : ")
    l.append(a)
    print("Name add sucessfully")

def remove_list():
    name=input("Enter name to remove : ")
    if name in l:
        l.remove(name)
        print("Name deleted sucessfully")
    else:
        print("Not found")

def search_list():
    s=input("Enter the name to search : ")
    if s in l:
        print("Name in list")
    else:
        print("Name not in list")

while True:
    print("                                    ")
    print("Choose Any one option")
    print("1. View student list")
    print("2. Add new name in list")
    print("3. Remove any name in list")
    print("4. Search any name")
    print("5. Exit")
    print("                                    ")

    ch=int(input("Enter you choice : "))
    if ch==1:
        open_list()
    elif ch==2:
        add_list()
    elif ch==3:
        remove_list()
    elif ch==4:
        search_list()
    elif ch==5:
        exit()
    else:
        print("Wrong input")

    b=input("Do you continue this (yes/no) : ")
    print("_"*40)
    print("_"*40)
    if (b=="yes"):
        continue
    elif(b=="no"):
        break
    
        
