n=int(input())
a,b=list(map(int,input().split())),list(map(int,input().split()));a.sort();b.sort()
print(sum([a[i]*b[-i-1]for i in range(n)]))