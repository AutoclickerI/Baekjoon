n,m=map(int,input().split())
x=y=0
a=[]
for i in range(n+m-1):
    if i%2:
        a+='DU'
        while x>0 and y<m-1:
            a+='R'
            y+=1
            if y<m-1:
                a+='U'
                x-=1
        if y<m-1:
            a+='R'
            y+=1
        if x+y&1==i&1:
            a+='D'
            x+=1
    else:
        a+='RL'
        while x<n-1 and y>0:
            a+='D'
            x+=1
            if x<n-1:
                a+='L'
                y-=1
        if x<n-1:
            a+='D'
            x+=1
        if x+y&1==i&1:
            a+='R'
            y+=1
print(*a,sep='')