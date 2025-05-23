i=1
while i:=int(input()):a=[0]*5;exec('s=int(input(),36)-20;a[[0<s<3,s>17,0,s==8,s==13,0,0,1].index(1)%5]+=1;'*i);print(*a)