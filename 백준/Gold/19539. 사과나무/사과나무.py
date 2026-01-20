s=sum(v-v%2*3for v in map(int,[*open(0)][1].split()))
print('YNEOS'[s|s%-3<0::2])