s=input()
l=1001
print(~-len({s[i%l:i//l]for i in range(l*l)}))