a=[int(input())for i in range(int(input()))]
try:
    b={1:[(a[0],0),(a[0],0)],2:[(a[1],0),(a[0]+a[1],1)]}
    for i in range(2,len(a)):
        b[i+1]=[(max(b[i-1][0][0],b[i-1][1][0])+a[i],0),(b[i][0][0]+a[i],1)]
    print(max(b[len(a)][0][0],b[len(a)][1][0]))
except:
    print(a[0])