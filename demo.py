import os
books={}
def add_book():
    isbn=input("Enter ISBN ....  ")
    title=input("Enter Title ....  ")
    author=input("Enter Author ....  ")
    books[isbn]={"Title":title,"Author":author,"Available":True}
    print(f"{title} by {author} with num {isbn} ISBN was added successfully....")
def ask_continue():
     choice2=input("Would u like to try again ? (Y/N)  ").capitalize()
     if choice2=="Y":
        return True
     else: 
        return False 
def display():
     for k in books:
      print(f"ISBN: {k} , AUTHOR: {books[k]["Author"]} , TITLE: {books[k]["Title"]} , AVAILABLE: {books[k]["Available"]}")
     choice2=input("Press Enter to go back to the main menu")
while True:
    choice1=input("""menu:
1-Add book
2-Check out book
3-Check in book
4-Show list
5-Exit
plz enter your choice (1 to 5)""")
    if choice1=="5":
        print("Exiting..............")
        break
    elif choice1 not in ["1","2","3","4","5"]:
        print("Invalid choise.......")
        continue
    elif choice1=="1":
        while True:
            os.system("cls")    
            add_book()
            if ask_continue()== False :
                break
    elif choice1=="2":
        while True:
            os.system("cls")
            isbn=input("Enter ISBN to check out ....  ")
            if isbn in books:
                books[isbn]["Available"]=False
                print(f"book {books[isbn]['Title']} checked out successfully.")
                if ask_continue()== False :
                  break
            elif isbn not in books:
                print("Sorry we dont have such a book now ....")
                if ask_continue()== False :
                 break
    elif choice1=="4":
            os.system("cls")
            display()
    elif choice1=="3":
        while True:
            os.system("cls")
            isbn=input("Enter ISBN to check in.... ")
            if isbn in books:
                books[isbn]["Available"]=True
                print(f"{books[isbn]["Title"]} was returned to the library successfully ")
                if ask_continue()== False :
                 break
            else:
                print("book not found.....")
                if ask_continue()== False :
                 break
            