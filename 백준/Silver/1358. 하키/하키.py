W,H,X,Y,P=map(int,input().split())
s=0
for i in[0]*P:
    x,y=map(int,input().split())
    if(X<=x<=X+W)*(Y<=y<=Y+H)or min((x-X)**2+(y-Y-H/2)**2,(x-X-W)**2+(y-Y-H/2)**2)<=H*H/4:
        s+=1
print(s)