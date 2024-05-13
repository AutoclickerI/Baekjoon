l=input().split()        
s=input()
print(sum(i.startswith(s)*len(i)>len(s)for i in l))