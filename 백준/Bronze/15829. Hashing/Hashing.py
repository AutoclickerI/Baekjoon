_,s=open(0)
print(sum((ord(s[i])-96)*31**i for i in range(len(s)-1))%1234567891)