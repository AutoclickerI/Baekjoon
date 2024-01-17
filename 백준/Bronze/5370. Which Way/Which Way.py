for i in map(int,open(0)):
    n=i.bit_length()-i.bit_count()*2+(i==0)
    if n==0:
        print('straight')
    if n>0:
        print('left')
    if n<0:
        print('right')