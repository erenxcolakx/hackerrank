n = int(input().strip())
l=''
while n != 1 and n != 0:
    l=l+str(n % 2)
    n=n//2    
else:
    l=l+str(n)
l=l[::-1]
print(len(max(l.split("0"))))