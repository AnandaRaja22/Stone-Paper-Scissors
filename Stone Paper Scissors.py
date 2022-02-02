import random
Your_Points =0
computer =0
while Your_Points <=3 and computer<=3:
    print("\n1.Stone\n2.Paper\n3.Scissors\n*****")
    user=int(input("Select any input: "))
    if user==1 or user==2 or user==3:
        if user==1:
            a='Stone'
        elif user==2:
            a='Paper'
        else:
            a='Scissors'
        game=[1,2,3]
        comp=random.choice(game)
        if comp==1:
            b='Stone'
        elif comp==2:
            b='Paper'
        else:
            b='Scissors'
        print("User = ",a,"\nComputer = ",b,"\n")
        if(user==comp):
            print("Game Draw\nScore : ",Your_Points,":",computer)
        elif user==1 and comp!=2 :
            Your_Points += 1
            print("User Wins!!\n",Your_Points,":",computer)
        elif user==2 and comp!=3 :
            Your_Points+=1
            print("User Wins!!\nScore : ",Your_Points,":",computer)
        elif user==3 and comp!=1 :
            Your_Points+=1
            print("User Wins!!\nScore : ",Your_Points,":",computer)
        else:
            computer+=1
            print("Computer Wins!!\nScore : ",Your_Points,":",computer)
        if Your_Points==3:
            print("Congratulations You Won The Game\n--------------------------------------------------\n")
            print("Press 1 to Play Again!\nPress 0 to exit")
            val=int(input())
            if val==0:
                print("Game Over")
                break
            else:
                Your_Points=0
                computer=0
        elif computer==3:
            print("Sorry!! Better Luck next time\n---------------------------------------------------\n")
            print("Press 1 to Play Again!\nPress 0 to exit")
            val = int(input())
            if val == 0:
                print("Game Over")
                break
            else:
                Your_Points = 0
                computer = 0
    else:
        print("Enter only 1 or 2 or 3")
        print("Score : ", Your_Points, ":", computer)
