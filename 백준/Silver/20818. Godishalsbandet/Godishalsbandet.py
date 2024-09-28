n=len(s:=[i:=0]+[i:=i+(j=='B')for j in input()*2])//2
print(max(s[i+n//2]-s[i]for i in range(n)))