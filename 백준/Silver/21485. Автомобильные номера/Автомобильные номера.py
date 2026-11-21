from itertools import*
P=permutations
S=input()
print(len(a:={''.join((s[0],*t,*s[1:]))for s,t in product(P(S[0]+S[4:]),P(S[1:4]))}))
print(*a,sep='\n')