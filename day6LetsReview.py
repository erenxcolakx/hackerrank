T = int(input("give input number:"))
wordList=[]
for i in range(0,T):
    print("Enter an input: ")
    S = str(input())
    wordList.append(S)    
for c in wordList:
    even=[]
    odd = []
    for chars in range(len(wordList)):
        if (chars % 2 == 0):
            even.append(wordList[c][chars])
        else:
            odd.append(wordList[c][chars])
    print("".join(even),"".join(odd))     
#-------------------------------  
T = int(input("give input number:"))
wordList=[]
for i in range(0,T):
    print("Enter an input: ")
    S = str(input())
    wordList.append(S)    
for c in wordList:
    even=[]
    odd = []
    for chars in range(len(c)):
        if (chars % 2 == 0):
            even.append(c[chars])
        else:
            odd.append(c[chars])
    print("".join(even),"".join(odd))  
    print(c)     
    
