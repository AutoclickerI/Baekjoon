key=input()
l=[[]for _ in[0]*len(key)]
cnt=0
for i in input():
    if i.isalpha():
        l[cnt]+=i,
        cnt=-~cnt%len(key)
for i in range(len(key)):
    shift=ord(key[i])-65
    for j in range(len(l[i])):
        l[i][j]=chr(((ord(l[i][j])-65)+shift)%26+65)
try:
    cnt=0
    while 1:
        print(end=l[cnt].pop(0))
        cnt=-~cnt%len(key)
except:0