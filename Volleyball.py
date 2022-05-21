print("Players in the group:")
s="PRASSANA,NARASIMHA,PRANAV,NAVEEN,VARUN,VENKAT,HARSHITH,RIZWAN,GAJANI,MADANI,TARUN,YUNUS"
s=s.split(",")
print(s,type(s))
while(True):
    a = input("Are there any other players who are interested to join the game(yes/no):")
    a = a.lower()
    if(a=="yes") or (a=="no"):
            break
    print("Please enter a valid input (yes/no)")
if(a=="yes"):
    p=int(input("Enter the no of extra players who are interested to join the game:"))
    for i in range(1,p+1):
        name=input("Enter the {} player name:".format(i))
        s.append(name)
    print(s)
while(True):
    n = int(input("Enter number of players who will attend on this weekend(21-22 May):"))
    if (n>=0):
        break
    print("{} is Invalid Input, please enter a valid input".format(n))
if(n>=10) and (n<=14):
        print("Lets play volleyball and have fun.")
elif(n>=6) and (n<10):
        print("Lets try for atleast 10 players and play volleyball")
elif(n>15):
        print("This cannot be happen,if it happens we will have a good game")
else:
        print("Take rest at home and play with kids")