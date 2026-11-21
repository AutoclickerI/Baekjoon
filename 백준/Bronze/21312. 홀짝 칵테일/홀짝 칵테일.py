l=input().split()
print(eval('*'.join([i for i in l if int(i)%2]or l)))