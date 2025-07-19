f=lambda h:int(h[0])*12+int(h[2:-1])
for T in range(int(input())):c,a,b=input().split();s=f(a)+f(b)-ord(c)%2*10+5;l,r=s-7>>1,s+8>>1;print(f"Case #{T+1}: {l//12}'{l%12}\" to {r//12}'{r%12}\"")