n= int(input())
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
    if n==0 and s>9:
        n=s
        s=0
print(s)
 