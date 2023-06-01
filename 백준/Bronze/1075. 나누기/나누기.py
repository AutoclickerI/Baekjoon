a=int(input())//100*100
b=int(input())
c=b-a%b if a%b else 0
print(c if c>9 else '0'+str(c))
