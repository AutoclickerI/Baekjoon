l=sorted(map(int,input().split()))
if l[0]-l[1]==l[1]-l[2]:
    print(2*l[2]-l[1])
else:
    if l[0]-l[1]>l[1]-l[2]:print(2*l[1]-l[0])
    else:print(2*l[1]-l[2])