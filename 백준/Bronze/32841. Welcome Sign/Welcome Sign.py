r,c=map(int,input().split())
f=0
for _ in[0]*r:
    s=input()
    l=c-len(s)
    v=l+f>>1
    print('.'*v+s+'.'*(l-v))
    f^=l%2