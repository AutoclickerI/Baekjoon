*l,=map(int,input().split())
print(eval('*'.join(map(str,[i for i in l if i%2]or l))))