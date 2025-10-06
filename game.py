import random 
item_list=["Rock","Paper","Scissor"]
user_choice=input("enter your move=Rock,Paper,Scissor= ")
com_choice=random.choice(item_list)
print(f"User choice = {user_choice},computer choice={com_choice}")
if user_choice==com_choice:
    print("Both chooses same. Match Tied !!")
elif user_choice=='Rock':
    if com_choice=="Paper":
        print("Paper cover rock. computer wins")
    else :
        print("Rock smashes scissor.You win")

elif user_choice=="Paper":
    if com_choice=="Scissor":
        print("scissor cuts paper,Computer wins")
    else :
        print("Paper covers rock,you win")

elif user_choice=="Scissor":
    if com_choice=="Paper":
        print("scissor cut paper,you win ")
    else:
        print("rock smashes scissor,computer wins ")
