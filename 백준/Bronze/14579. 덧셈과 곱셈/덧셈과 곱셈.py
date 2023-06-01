a,b=map(int,input().split());s=1
print(eval('*'.join(str((i*i+i)//2)for i in range(a,b+1)))%14579)