T=0
def check(Z,I,M,L):
    s=set()
    while{L:=(Z*L+I)%M}-s:s|={L}
    return len(s)
while'1'<(i:=input()):T+=1;print(f'Case {T}:',check(*map(int,i.split())))