a=1
for i in sorted(map(eval,open(0)))[1:]:a*=i*10
print(a/362880)