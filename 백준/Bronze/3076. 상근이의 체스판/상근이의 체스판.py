r,c,a,b=map(int,open(i:=0).read().split())
while i-r*a:print(''.join(b*'X.'[j+i//a&1]for j in range(c)));i+=1