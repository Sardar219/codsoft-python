import random
User_Score=0;
Computer_Score=0
choices=['Rock','Paper','Scissors']
while True:
    computer=random.choice(choices);
    user=input("Rock Paper or Scissors choice one of them : ").capitalize()
    if user not in choices:
        print("You enter something wrong!")
    else:
        if computer==user:
            print(f"Computer choose {computer}\nYou choose {user}\nYou are equal.")
        elif computer=="Rock":
            if user=="Paper":
                print(f"Computer choose {computer}\nYou choose {user}\nYou are win!!!")
                User_Score+=1
            else:
                print(f"Computer choose {computer}\nYou choose {user}\nYou lost!!!")
                Computer_Score+=1
        elif computer=="Paper":
            if user=="Scissors":
                print(f"Computer choose {computer}\nYou choose {user}\nYou are win!!!")
                User_Score+=1
            else:
                print(f"Computer choose {computer}\nYou choose {user}\nYou lost!!!")
                Computer_Score+=1
        else:
            if user=="Rock":
                print(f"Computer choose {computer}\nYou choose {user}\nYou are win!!!")
                User_Score+=1
            else:
                print(f"Computer choose {computer}\nYou choose {user}\nYou lost!!!")
                Computer_Score+=1
    
    play=input("\nDo you want to continue for Yes \"Y\" for No \"N\" ? [Y/N] : ").upper()
    if play=="N":
        print("-----------------------------------------")
        print(f"In Totally\nYou can achieve {User_Score} score.\nThe Computer can achieve {Computer_Score} score.")
        if User_Score>Computer_Score:
            print("In Totally You Win !!!")
        elif User_Score<Computer_Score:
            print("In Totally You Lost !!!")
        else:
            print("In Totally You Equal")
        break
        
        
            
    