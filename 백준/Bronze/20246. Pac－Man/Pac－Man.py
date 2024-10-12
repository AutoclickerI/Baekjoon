x,y=map(int,input().split())
while x+y:
    print(x,y)
    if x:x-=1
    else:y-=1
    
for i in range(10):
    for j in range(10)[::1-i%2*2]:print(i,j)