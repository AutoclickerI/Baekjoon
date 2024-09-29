s=eval('input(),'*4)
def getpos(c):
    for y in 0,1,2,3:
        for x in range(10):
            if s[y][x]==c:return y,x
y=x=0
for i in input():
    a,b=getpos(i);y+=a;x+=b
print(s[y//9][x//9])