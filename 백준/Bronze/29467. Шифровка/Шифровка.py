R=range(len(s:=input()))
print(max({s[i:j+1]for i in R for j in R}))