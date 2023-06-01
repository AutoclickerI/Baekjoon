a=sorted(map(int,input().split()))
print('N'if(a[0]-a[1])*(a[1]-a[2])*(a[2]-a[1]-a[0])else'S')