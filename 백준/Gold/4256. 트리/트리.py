import sys
sys.setrecursionlimit(10**6)

class node:
    def __init__(self,cur):
        self.cur=cur
        self.left=None
        self.right=None

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.cur,end=' ')

def build(pre,ino):
    if pre:
        cur=node(pre[0])
        idx=0
        while ino[idx]!=pre[0]:
            idx+=1
        ino_left=ino[:idx]
        ino_right=ino[1+idx:]
        pre_left=pre[1:1+idx]
        pre_right=pre[1+idx:]
        cur.left=build(pre_left,ino_left)
        cur.right=build(pre_right,ino_right)
        return cur
    

for _ in[0]*int(input()):
    input()
    *preorder,=map(int,input().split())
    *inorder,=map(int,input().split())
    root=build(preorder,inorder)
    postorder(root)
    print()