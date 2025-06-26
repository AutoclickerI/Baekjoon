s,e=map(int,input().split())
print((s^-e)//2&1^(s%2*s^~e%2*e)&-2)