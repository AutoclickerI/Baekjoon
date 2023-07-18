n=int(input())+1
s=str(n)
l=len(s)
if l%2:
    t=s[:l//2+1]
    if t[::-1]<s[l//2:]:
        t=str(int(t)+1)
    print(t+t[::-1][1:])
else:
    t=s[:l//2]
    if t[::-1]<s[l//2:]:
        t=str(int(t)+1)
    print(t+t[::-1])