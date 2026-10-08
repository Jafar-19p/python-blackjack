import random
choices=["ACE",2,3,4,5,6,7,8,9,10,"J","K","Q"]
user_choice1,user_choice2,computer_choice1,computer_choice2=random.choices(choices,k=4)
total_user=[user_choice1,user_choice2]
total_computer=[computer_choice1,computer_choice2]
def convert(total_choices):
 for i in range(len(total_choices)):
     if total_choices[i]=="J" or total_choices[i]=="K" or total_choices[i]=="Q":
              total_choices[i]=10
     elif total_choices[i]=="ACE":
         total_choices[i]=11
 if sum(total_choices)>21:
     for i in range(len(total_choices)):
         if total_choices[i]==11:
             total_choices[i]=1
             break
convert(total_user)
convert(total_computer)
if sum(total_user)==21 and sum(total_computer)<21:
    print(f"You win your cards is {total_user} and current score is {sum(total_user)} ")
    print(f"The computer cards is {total_computer} ")
elif sum(total_user)<21 and sum(total_computer)==21: 
    print(f"Looser  your cards is {total_user} and current score is {sum(total_user)} ")
    print(f"The computer cards is {total_computer} ")
elif sum(total_user)==21 and sum(total_computer)==21:
    print("Its a drwa ")
else: 
    while sum(total_user)<21:
        print(f"Your cards are {total_user} , current score is {sum(total_user)} ")
        print(f"Computer first card is {total_computer[0]} ")
        hit=input("Get another card ? (y/n)").lower()
        if hit=="y":
            user_choice=random.choice(choices)
            total_user.append(user_choice)
            convert(total_user)
        elif hit=="n":
            break 
        else:
            print("Invaild input ")
            
    if sum(total_user)>21 :
        print(f"Your cards are {total_user} , current score is {sum(total_user)}")
        print(f"The computer cards is {total_computer} ")
        print("looser")
    else:
        while sum(total_computer)<17 : 
          computer_choice=random.choice(choices)
          total_computer.append(computer_choice)
          convert(total_computer)
        if sum(total_computer)>21:
            print(f"Your cards are {total_user} , current score is {sum(total_user)}")
            print(f"The computer cards is {total_computer} ")
            print(" Winer ")
        elif sum(total_computer)==sum(total_user):
            print(f"Your cards are {total_user} ,  score is {sum(total_user)}")
            print(f"The computer cards is {total_computer} , score is {sum(total_computer)}")
            print("Its a drwa ")
        elif sum(total_computer)<sum(total_user):
             print(f"Your cards are {total_user} ,  score is {sum(total_user)}")
             print(f"The computer cards is {total_computer} , score is {sum(total_computer)}")
             print(" Winer ")
        else:
            print(f"Your cards are {total_user} ,  score is {sum(total_user)}")
            print(f"The computer cards is {total_computer} , score is {sum(total_computer)}")
            print("looser  ")
    