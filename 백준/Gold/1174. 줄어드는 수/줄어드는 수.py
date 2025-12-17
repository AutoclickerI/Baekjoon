*l,=range(10)
for i in l:l+=[j+i*10for j in range(i%10)]
print((l+[-1]*6**8)[int(input())-1])