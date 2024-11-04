input()
b=input()
k=input()
B=input()
K=input()
k1=[i for i,s,S in zip(k,b,B)if s==S]
k2=[i for i,s,S in zip(K,b,B)if s==S]
if k1==k2:
    print(*k1,sep='')
else:
    print('htg!')