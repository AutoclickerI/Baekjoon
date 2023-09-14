from itertools import*
class paint:
    def __init__(self,r,g,b):
        self.r=r
        self.g=g
        self.b=b
        
    def __add__(self,p):
        return paint(self.r+p.r,self.g+p.g,self.b+p.b)
    
    def __truediv__(self,n):
        return paint(self.r//n,self.g//n,self.b//n)
    
    def __sub__(self,p):
        return abs(self.r-p.r)+abs(self.g-p.g)+abs(self.b-p.b)

n=int(input())
*l,r=[paint(*map(int,input().split()))for _ in[0]*-~n]
print(min(min(r-sum(i,paint(0,0,0))/len(i)for i in combinations(l,j))for j in range(2,min(n+1,8))))