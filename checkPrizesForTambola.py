def showBoard(board):
    for i in range(1,91):
        if(i==11 or i==21 or i==31 or i==41 or i==51 or i==61 or i==71 or i==81 or i==91):
            print()
        if(i in board):
            print(i,end="\t")
        else:
            print("\t")


def isEarly7(arr,board):
    ctr=0
    if(len(arr)<7):
        return 0
    else:
        for i in arr:
            if(i in board):
                ctr+=1
    if(ctr>=7):
        return 1
    else:
        return 0
    
def isTemperature(arr,board):
    t1=arr[0]
    t2=arr[14]
    if((t1 in board) and (t2 in board)):
        return 1
    else:
        return 0
    
def isFirstLine(arr,board):
    ctr=0
    for i in range(5):
        if(arr[i] in board):
            ctr+=1
    if(ctr==5):
        return 1
    else:
        return 0


def isMiddleLine(arr,board):
    ctr=0
    for i in range(5,10):
        if(arr[i] in board):
            ctr+=1
    if(ctr==5):
        return 1
    else:
        return 0

    
def isLastLine(arr,board):
    ctr=0
    for i in range(10,15):
        if(arr[i] in board):
            ctr+=1
    if(ctr==5):
        return 1
    else:
        return 0


def isCorners(arr,board):
    ctr=0
    c1=arr[0]
    c2=arr[4]
    c3=arr[10]
    c4=arr[14]
    if((c1 in board) and (c2 in board) and (c3 in board) and (c4 in board)):
        return 1
    else:
        return 0


def isBreakfast(arr,board):
    flag=0
    for i in arr:
        if(i<=30 and (i not in board)):
            flag=0
            break
        else:
            flag=1
    if flag==0:
        return 0
    else:
        return 1

def isLunch(arr,board):
    flag=0
    for i in arr:
        if(i>30 and (i<=60) and (i not in board)):
            flag=0
            break
        else:
            flag=1
    if flag==0:
        return 0
    else:
        return 1

def isDinner(arr,board):
    flag=0
    for i in arr:
        if(i>60 and (i not in board)):
            flag=0
            break
        else:
            flag=1
    if flag==0:
        return 0
    else:
        return 1

def isFullHouse(arr,board):
    flag=0
    for i in arr:
        if(i not in board):
            flag=0
            break
        else:
            flag=1
    if(flag==1):
        return 1
    else:
        return 0




board=set()
tickets=dict()
totalTickets=int(input("Enter no of tickets to be checked for"))
for i in range(totalTickets):
    tkts=list(map(int,input("Enter numbers Row wise ").split()))
    tickets[i+1]=tkts
    



print(tickets)


for i in range(90):
    n=int(input("Enter new number generated"))
    board.add(n)
    for j in range(totalTickets):
        tkt=tickets[j+1]
        Early = isEarly7(tkt,board)
        First = isFirstLine(tkt,board)
        Middle = isMiddleLine(tkt,board)
        Last = isLastLine(tkt,board)
        Corner = isCorners(tkt,board)
        Breakfast = isBreakfast(tkt,board)
        Lunch = isLunch(tkt,board)
        Dinner = isDinner(tkt,board)
        Temperature = isTemperature(tkt,board)
        Full = isFullHouse(tkt,board)
        print()
        if(Early == 1):
            print("Early 7 for Ticket :",j+1)
        if(First == 1):
            print("First Line for Ticket :",j+1)
        if(Middle == 1):
            print("Middle Line for Ticket :",j+1)
        if(Last == 1):
            print("Last Line for Ticket :",j+1)
        if(Corner == 1):
            print("Corner for Ticket :",j+1)
        if(Breakfast == 1):
            print("Breakfast for Ticket :",j+1)
        if(Lunch == 1):
            print("Lunch for Ticket :",j+1)
        if(Dinner == 1):
            print("Dinner for Ticket :",j+1)
        if(Temperature == 1):
            print("Temperatue for Ticket :",j+1)
        if(Full == 1):
            print("Full House for Ticket :",j+1)
        print()





        
