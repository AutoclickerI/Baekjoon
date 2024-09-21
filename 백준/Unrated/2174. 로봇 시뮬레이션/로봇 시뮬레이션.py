def main():
    A,B=map(int,input().split())
    N,M=map(int,input().split())
    
    d={}
    p=set()
    
    for i in range(N):
        x,y,pi=input().split()
        d[i+1]=[int(y)-1,int(x)-1,'NESW'.find(pi)]
        p.add((int(y)-1,int(x)-1))
    
    for idx in range(M):
        a,b,c=input().split()
        if b=='R':
            d[int(a)][2]=d[int(a)][2]+int(c)&3
        if b=='L':
            d[int(a)][2]=d[int(a)][2]+3*int(c)&3
        if b=='F':
            c=int(c)-1
            y,x,di=d[int(a)]
            dy,dx={0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)}[di]
            p.remove((y,x))
            y+=dy
            x+=dx
            while c and (y,x)not in p and 0<=y<B and 0<=x<A:
                c-=1
                y+=dy
                x+=dx
            if c or not (0<=y<B and 0<=x<A) or (y,x)in p:
                if (y,x)not in p:
                    print('Robot',a,'crashes into the wall')
                    for _ in range(idx+1,M):
                        input()
                    break
                else:
                    print('Robot',a,'crashes into robot',[i for i in d if tuple(d[i][:2])==(y,x)][0])
                    for _ in range(idx+1,M):
                        input()
                    break
            else:
                p.add((y,x))
                d[int(a)]=[y,x,di]
    else:
        print('OK')

main()