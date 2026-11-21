from datetime import*
D=datetime
c=D.strptime(input(),'%B %d, %Y %H:%M')
s=D(y:=c.year,1,1)
print(100*(c-s)/(D(y+1,1,1)-s))