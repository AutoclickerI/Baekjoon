n=int(input())
l=[input()for _ in[0]*n]
def quad(x,y,s):
    t=l[x][y]
    for i in range(x,x+s):
        for j in range(y,y+s):
            if l[i][j]!=t:
                return'('+quad(x,y,s//2)+quad(x,y+s//2,s//2)+quad(x+s//2,y,s//2)+quad(x+s//2,y+s//2,s//2)+')'
    return t
print(quad(0,0,n))