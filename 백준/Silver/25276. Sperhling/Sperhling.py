a,b=input(),input()
i=0
while i<min(len(a),len(b))!=a[i]==b[i]:i+=1
print(len(a)+len(b)-2*i)