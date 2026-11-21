[N],*bites,parity=[[*map(int,i.split())]for i in open(0)]

byte_check=[sum(i)%2for i in bites]
if byte_check.count(0) == 1:
    print('Odd')
    bite = byte_check.index(0) + 1
else:
    print('Even')
    bite = byte_check.index(1) + 1

bites.append(parity)
bits = [*map(list, zip(*bites))]
bit_check = [sum(line) % 2 for line in bits]
if bit_check.count(0) == 1:
    bit = bit_check.index(0) + 1
else:
    bit = bit_check.index(1) + 1


print('Byte',bite,'is broken')
print('Bit',bit,'is broken')