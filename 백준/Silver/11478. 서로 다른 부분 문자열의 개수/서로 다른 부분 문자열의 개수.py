l=len(s:=input())
print(len({s[i//l:][:i%l]for i in range(l*l)}))