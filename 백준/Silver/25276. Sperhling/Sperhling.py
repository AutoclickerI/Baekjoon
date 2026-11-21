a=input()+'1'
b=input()+'2'
i=0
while a[i]==b[i]:i+=1
print(len(a)+len(b)+~i*2)