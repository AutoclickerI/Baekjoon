s,e=map(int,input().split())
print(sum(len(i)==len({*i}-{'0'})==sum(int(i)%int(j)<1for j in i)for i in map(str,range(s,e+1))))