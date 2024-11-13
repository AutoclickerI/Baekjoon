import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

class node:
    def __init__(self,s,left=None,right=None,parent=None):
        self.value=int(s.split('/')[1])
        self.s=s
        self.left=left
        self.right=right
        self.parent=parent
    def __repr__(self):
        return f"node('{self.s}')"
    def __str__(self):
        return self.s


def printnode(node):
    if node:
        print(end='(')
        printnode(node.left)
        print(end=str(node))
        printnode(node.right)
        print(end=')')
    
    
while 1:
    n,*l=input().split()
    if n=='0':
        break
    root,*l=sorted(map(node,l),key=lambda n:n.s.split('/')[0])
    for i in l:
        if root.value<i.value:
            i.left=root
            root.parent=i
            root=i
        else:
            tmp=root
            while i.value<tmp.value and tmp.right:
                tmp=tmp.right
            if i.value<tmp.value:
                tmp.right=i
                i.parent=tmp
            else:
                i.left=tmp
                tmp.parent.right=i
                i.parent=tmp.parent
                tmp.parent=i
    printnode(root)
    print()