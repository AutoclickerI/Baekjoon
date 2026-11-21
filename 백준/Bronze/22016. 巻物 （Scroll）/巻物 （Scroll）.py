K,T=int(input().split()[1])-1,input()
print(T[:K],*[chr(ord(i)^32)for i in T[K:]],sep='')