p,q,r=map(int,input().split())
r+=q*2+p*3
if r>7:print('Province or',end=' ')
elif r>4:print('Duchy or',end=' ')
elif r>1:print('Estate or',end=' ')
if r>5:print('Gold')
elif r>2:print('Silver')
else:print('Copper')