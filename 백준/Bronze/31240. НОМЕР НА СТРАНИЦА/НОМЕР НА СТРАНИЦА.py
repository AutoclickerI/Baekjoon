l=len(S:=input())
v=l//2
a=0
for i in range(l-1>>1):a+=S[0]>'0'<S[i+1]
print(a+(S[:v]<=S[v:]!=l%2<1!=S[0]>'0'<S[v]))