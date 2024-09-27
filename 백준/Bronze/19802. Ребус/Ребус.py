a = ''
for s in input().split():
    i=j=0
    while s[i]=="'":i+=1
    while s[j-1]=="'":j-=1
    a+=s[2*i:2*j+len(s)]
print(a)