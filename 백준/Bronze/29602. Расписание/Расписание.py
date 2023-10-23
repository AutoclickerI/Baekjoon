input()
print(*[i for _,i in sorted((j,k+1)for k,j in enumerate(map(int,input().split())))])