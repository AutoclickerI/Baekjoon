w,U,D,L,R,A,V,S,E=map(open(0).read().count,'#UDLRAVSE')
print([-1,4-(A<1)*(1-(V<1)*~(w<2>U+D+L+R))][S==E==1])