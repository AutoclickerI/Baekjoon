l=k=['1']
exec("l+=(k:=sorted({j for i in k for j in[i[:2]+'0'+i[2:],i[:2]+'1'+i[2:]]if int(j)%2**len(j)==int(j,2)}));"*160)
print(l[int(input())-1])