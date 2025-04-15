N=int(input())

class node:
    def __init__(self,s):
        self.s=s
        self.child=[]
    def add(self,v):
        if v==[]:
            return
        for i in self.child:
            if i.s==v[0]:
                i.add(v[1:])
                break
        else:
            self.child+=node(v[0]),
            self.child[-1].add(v[1:])
    def __repr__(self):
        return f'node({self.s},{self.child})'
    def print(self,i):
        print('-'*i+self.s)
        for j in sorted(self.child,key=lambda s:s.s):
            j.print(i+2)
        

root=node(None)

for _ in[0]*N:
    _,*l=input().split()
    root.add(l)

for i in sorted(root.child,key=lambda s:s.s):
    i.print(0)