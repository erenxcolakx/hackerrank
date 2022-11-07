a = 0
inputnumber = int(input())
sozluk={}
while a < inputnumber:
    a=a+1
    nameAndNumber=str(input())
    splitList=nameAndNumber.split()
    sozluk[splitList[0]]=splitList[1]
while True:
    try:
        names=str(input())
        if sozluk.get(names,"Not found") == "Not found":
            print(sozluk.get(names,"Not found") , end="\n",sep="")
        else:
            print(names,"="+sozluk.get(names,"Not found") , end="\n",sep="")
    except EOFError:
        break
        
'''
inputs
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
'''   

'''
Expected Output
sam=99912222
Not found
harry=12299933
''' 
    