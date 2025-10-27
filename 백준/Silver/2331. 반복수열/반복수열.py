A,P=map(int,input().split())
s=set()
while A not in s:
    s|={A}
    A=sum(int(i)**P for i in str(A))
while A in s:
    s-={A}
    A=sum(int(i)**P for i in str(A))
print(len(s))