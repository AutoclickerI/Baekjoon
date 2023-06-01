while[0,0,0]!=(l:=[*map(int,input().split())]):
    if l[1]-l[0]==l[2]-l[1]!=0:
        print('AP',2*l[2]-l[1])
    else:
        print('GP',l[2]**2//l[1])