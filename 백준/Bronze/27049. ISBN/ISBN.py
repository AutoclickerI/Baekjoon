s=input()
a=-1
for j in range(10+(s[9]=="?")):sum((10-i)*int([s[i],j,10][('>'<s[i])+(s[i]>'?')])for i in range(10))%11or(a:=j)
print([a,'X'][a>9])