p,q=map(int,input().split())
print(max(int(str(p*-~i)[::-1])for i in range(q)))