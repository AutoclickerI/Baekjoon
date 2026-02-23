import hashlib
s=[*open(0)][1]

h=hashlib.sha256(s.encode('utf-8')).hexdigest()
start='58c0000000000000000000000000000000000000000000000000000000000000'
mid  ='58e0000000000000000000000000000000000000000000000000000000000000'
end  ='5900000000000000000000000000000000000000000000000000000000000000'

assert start<=h<mid

n,*l=map(int,s.split())
v=[([n],[0])]
for i in l:
    n,[m]=v[-1]
    if m<n[0]:
        m-=i
    else:
        n,m=[i],0
    v+=(n,[m]),
print(max(i[0]-j[0]for i,j in v))