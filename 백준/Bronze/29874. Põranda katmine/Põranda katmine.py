g=lambda:[*map(int,input().split())]
(X,Y),S,T=g(),g(),g()
ans="EI SAA"
if sorted([X, Y])==sorted(S):ans=f"0 0 {X} {Y}\nZ"
elif sorted([X, Y])==sorted(T):ans=f"Z\n0 0 {X} {Y}"
else:
    for i,j in[0,0],[0,1],[1,0],[1,1]:
        A1,B1,A2,B2=S[i],S[i^1],T[j],T[j^1]
        if A1==X==A2 and Y<=B1+B2 and B1<Y>B2:ans=f"0 0 {X} {B1}\n0 {Y - B2} {X} {Y}";break
        if B1==Y==B2 and X<=A1+A2 and A1<X>A2:ans=f"0 0 {A1} {Y}\n{X - A2} 0 {X} {Y}";break
print(ans)