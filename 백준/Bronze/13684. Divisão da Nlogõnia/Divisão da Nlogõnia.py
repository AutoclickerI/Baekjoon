while n:=int(input()):
    p,q=map(int,input().split())
    for _ in[0]*n:
        x,y=map(int,input().split())
        if x==p or y==q:print('divisa')
        elif x>p and y>q:print('NE')
        elif x>p and y<q:print('SE')
        elif x<p and y>q:print('NO')
        else:print('SO')