n= int(input())
if n<0:
    t= -n
else:
    t=n
rev=0
while t>0:
    r=t%10
    rev= rev*10 +r
    t=t//10
if n<0:
    print(-rev)
else:
    print(rev)