n=int(input())-1
t2=2**.5
x,y=map(int,input().split())
for _ in[0]*n:
    p,q=input().split()
    q=int(q)
    if p=='N':
        y+=q
    if p=='E':
        x+=q
    if p=='W':
        x-=q
    if p=='S':
        y-=q
    if p=='NE':
        x+=q/t2
        y+=q/t2
    if p=='SE':
        x+=q/t2
        y-=q/t2
    if p=='SW':
        x-=q/t2
        y-=q/t2
    if p=='NW':
        x-=q/t2
        y+=q/t2
print(f'{x:.6f} {y:.6f}')