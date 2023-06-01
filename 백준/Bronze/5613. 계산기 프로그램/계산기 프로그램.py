a=input()
while((l:=input())!='='):a=str(eval((a+l+input()).replace('/','//')))
print(a)