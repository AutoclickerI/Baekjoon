N,A,B=map(int,input().split())
if N<=B:
    if A==B:print('Anything')
    elif A>B:print('Subway')
    else:print('Bus')
else:
    print('Bus')