l=[]
for i in range(5):
    if'FBI'in input():
        l+=[i+1]
print(*l if l else['HE GOT AWAY!'])