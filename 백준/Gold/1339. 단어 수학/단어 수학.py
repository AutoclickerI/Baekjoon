v=[0]*26
for c in[0]*int(input()):
    s=input()
    for i in s[::-1]:
        v[ord(i)-65]+=10**c
        c+=1
print(sum(i*j for i,j in enumerate(sorted(v)[-10:])))