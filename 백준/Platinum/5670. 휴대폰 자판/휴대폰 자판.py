import sys
input=lambda:sys.stdin.readline().strip()

class node:
    def __init__(self):
        self.d={}
        self.cnt=0
    def add(self,s):
        self.cnt+=1
        if s:
            self.d[s[0]]=self.d.get(s[0],node())
            self.d[s[0]].add(s[1:])

def traverse(n):
    r=0
    if 1<len(n.d):
        r+=n.cnt-n.d.get('.',node()).cnt
    for i in n.d:
        r+=traverse(n.d[i])
    return r
try:
    while 1:
        N=int(input())
        b=[input()for _ in[0]*N]
        root=node()
        for i in b:root.add(i+'.')
        r=0
        for i in root.d:r+=traverse(root.d[i])+root.d[i].cnt
        print(f'{r/N:.2f}')
except:
    pass