n=len(S:=input())//2
a=n-S[1:n].count('0')-(S[n]<'1'or~len(S)%2and int(S[:n])>int(S[n:]))
print(int(S[0])and a)