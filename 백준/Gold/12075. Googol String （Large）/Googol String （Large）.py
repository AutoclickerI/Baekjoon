def get(k):
    if k<3:
        return 0
    if 2**k.bit_length()-k==k:
        return 0
    return 1^get(2**k.bit_length()-k)

for n in[*open(i:=0)][1:]:
    i+=1
    print(f'Case #{i}:',get(int(n)))