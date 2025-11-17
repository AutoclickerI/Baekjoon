_,h,k,*l=map(int,open(0).read().split())
h*=[0]
for i in l:h[0]+=i;h.sort()
print('WGAOI T'[k<h[0]::2])