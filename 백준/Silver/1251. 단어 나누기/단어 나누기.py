s=input()[::-1]
print(min(s[j:]+s[i:j]+s[:i]for j in range(len(s))for i in range(1,j)))