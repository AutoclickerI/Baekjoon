Y,M,D,T,P=[2*i-j for i,j in zip(map(eval,input().split()),map(eval,input().split()))]

Z=Y*360+M*30+D-31
print('%d %d %d %.3f %.3f'%(Z//360,Z//30%12+1,Z%30+1,T,P))