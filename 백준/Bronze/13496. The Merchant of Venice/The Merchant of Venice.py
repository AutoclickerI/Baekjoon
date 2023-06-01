for i in range(int(input())):
    p,q,r=map(int,input().split())
    l=0
    for j in[0]*p:
     o,h=map(int,input().split())
     l+=0 if o>q*r else h
    print(f'Data Set {i+1}:\n{l}\n')