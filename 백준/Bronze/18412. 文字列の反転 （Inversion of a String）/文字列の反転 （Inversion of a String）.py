p,q,r=map(int,input().split())
s=input()
print(s[:q-1]+s[q-1:r][::-1]+s[r:])