input()
*A,=map(int,input().split())
input()
*B,=map(int,input().split())
v=[]
while s:={*A}&{*B}:
    s=max(s)
    v+=s,
    A=A[A.index(s)+1:]
    B=B[B.index(s)+1:]
print(len(v))
print(*v)