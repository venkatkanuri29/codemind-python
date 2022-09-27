x,y= map(int,input().split())
if x+1==y or y+1==x or (x==1 and y==10) or (x==10 and y==1):
    print("Yes")
else:
    print("No")