import os
books={}
while True:
    choise1=input("""menu:
1-Add book
2-Check out book
3-Check in book
4-Show list
5-Exit
plz enter your choice (1 to 5)""")
    if choise1=="5":
        print("Exiting..............")
        break
    elif choise1 not in ["1","2","3","4","5"]:
        print("Invail choise.......")
        continue
    elif choise1=="1":
        while True:
            os.system("cls")    
            isbn=input("Enter ISBN ....  ")
            title=input("Enter Title ....  ")
            author=input("Enter Author ....  ")
            books[isbn]={"Title":title,"Author":author,"Available":True}
            print(f"{title} by {author} with num {isbn} ISBN was added sucsessfully....")
            choise2=input("Whould u like to add new one ? (Y/N)  ").capitalize()
            if choise2=="Y":
                continue
            else: 
                break 
    elif choise1=="2":
        while True:
            os.system("cls")
            isbn=input("Enter ISBN to check out ....  ")
            if isbn in books:
                books[isbn]["Available"]=False
                print(f"book {books[isbn]["Author"]} checked out successfully.")
                choise2=input("Whould u like to check out another one ? (Y/N)").capitalize()
                if choise2=="Y":
                    continue
                else: 
                    break
            elif isbn not in books:
                print("Sorry we dont have such a book now ....")
                choise2=input("Whould u like to check out another book ? (Y/N)").capitalize()
                if choise2=="Y":
                    continue
                else:
                    break 
    elif choise1=="4":
        while True:
            os.system("cls")
            for k in books:
                print(f"ISBN: {k} , AUTHOR: {books[k]["Author"]} , TITLE: {books[k]["Title"]} , AVAILABLE: {books[k]["Available"]}")
            choise2=input("Press Enter to go back to the main menu")
            break
    elif choise1=="3":
        while True:
            os.system("cls")
            isbn=input("Enter ISBN to check in.... ")
            if isbn in books:
                books[isbn]["Available"]=True
                print(f"{books[isbn]["Title"]} was return to the library successfully ")
                s=input("would u like to chick in another book ? (Y/S)")
                if s=="y":
                    continue 
                else:
                    break
            else:
                print("book not found.....")
                s=input("Do u want to chick in another book ? (Y/N)").capitalize()
                if s=="":
                 continue 
                else:
                 break
            