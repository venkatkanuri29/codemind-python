n= int(input())
i=1
s=0
while i<n:
    if  n%i==0:
        s +=i
        i=i+1
    else :
        i+=1
print(s==n)