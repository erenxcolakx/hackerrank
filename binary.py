Number = int(input().strip())
l=''
while Number != 1 and Number != 0:
    l=l+str(Number%2)
    Number=Number//2    
else:
    l=l+str(Number)
print(l[::-1])
