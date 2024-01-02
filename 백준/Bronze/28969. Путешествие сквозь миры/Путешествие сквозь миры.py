s,e=map(int,input().split())
print(sum(s<=int(-~i*str(-~j))<=e for i in range(18)for j in range(9)))