*s,=input()
k=s.index('*')
s[k]=0
print(sum(map(int,2*s[1::2]+s))*(k%2*4-1)%10)