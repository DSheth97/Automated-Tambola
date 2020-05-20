def GenerateTicket():
    from random import randint
    from random import sample
    import numpy
    arr=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    ctr=[0,0,0,0,0,0,0,0,0]

    
    seq1=[i for i in range(1,9)]
    seq2=[i for i in range(10,19)]
    seq3=[i for i in range(20,29)]
    seq4=[i for i in range(30,39)]
    seq5=[i for i in range(40,49)]
    seq6=[i for i in range(50,59)]
    seq7=[i for i in range(60,69)]
    seq8=[i for i in range(70,79)]
    seq9=[i for i in range(80,90)]
    
    
    #print(col1set)
    
    for i in range(3):
        for j in range(9):
            if(j==0):
                arr[i][j] = sample(seq1,k=1)[0]
                seq1.remove(arr[i][j])
            elif(j==1):
                arr[i][j] = sample(seq2,k=1)[0]
                seq2.remove(arr[i][j])
            elif(j==2):
                arr[i][j] = sample(seq3,k=1)[0]
                seq3.remove(arr[i][j])
            elif(j==3):
                arr[i][j] = sample(seq4,k=1)[0]
                seq4.remove(arr[i][j])
            elif(j==4):
                arr[i][j] = sample(seq5,k=1)[0]
                seq5.remove(arr[i][j])
            elif(j==5):
                arr[i][j] = sample(seq6,k=1)[0]
                seq6.remove(arr[i][j])
            elif(j==6):
                arr[i][j] = sample(seq7,k=1)[0]
                seq7.remove(arr[i][j])
            elif(j==7):
                arr[i][j] = sample(seq8,k=1)[0]
                seq8.remove(arr[i][j])
            elif(j==8):
                arr[i][j] = sample(seq9,k=1)[0]
                seq9.remove(arr[i][j])
            else:
                print("Error generating ticket") 
    #showTicket(arr)
    lst=numpy.transpose(arr)
    #print(lst)
    for j in range(9):
        lst[j].sort()
        
    #print(lst)
    tkt = numpy.transpose(lst)
    #showTicket(tkt)

    #removeSeq=[i for i in range(8)]
    
    for i in range(3):
        removeSeq=[z for z in range(9)]
        j=0
        while(j<=3):
            if((i==2) and (0 in ctr)):      #To not have 3 numbers in single column
                s = ctr.index(0)
                removeSeq.remove(s)
            else:
                s=sample(removeSeq,k=1)[0]
                removeSeq.remove(s)
            
            if(ctr[s]<2):
                tkt[i][s]=0
                ctr[s]+=1
            else:
                j=j-1
            j=j+1
    showTicket(tkt)
    return tkt
                


    
def showTicket(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(arr[i][j]!=0):
                print(arr[i][j],end="\t")
            else:
                print(" ",end="\t")
        print()



def GenerateRandomButton(arr):
  
    k=randint(1,90)
    if(k not in arr):
        return k
    else:
        return GenerateRandomButton(arr)


def isEarly7(arr,board):
    flag=0
    if(len(arr)<7):
        return 0
    else:
        for i in arr:
            if(i not in board):
                return 0
            else:
                flag=1
    if(flag==1):
        return 1
    else:
        return 0



def convertTicket2Dto1D(arr):
    lst=[]
    for i in arr:
        for j in i:
            if(j!=0):
                lst.append(j)
    return lst

def showBoard(board):
    for i in range(1,91):
        if(i==11 or i==21 or i==31 or i==41 or i==51 or i==61 or i==71 or i==81 or i==91):
            print()
        if(i in board):
            print(i,end="\t")
        else:
            print("\t")





# generatedTicket = GenerateTicket()
# convertedTicket = convertTicket2Dto1D(generatedTicket)
# print(convertedTicket)
# board=set()
# for m in range(90):
#     newno = GenerateRandomButton(board)
#     board.add(newno)
#     showBoard(board)
#     e=isEarly7(convertedTicket,board)
#     if(e==1):
#         print("YAY! Early 7")
#     else:
#         print("Not Early 7 yet")





    
    
