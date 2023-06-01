i=1
for _ in[0]*int(input()):
    p,q,r=sorted(map(int,input().split()))
    if p+q>r:a=2-(p==q or q==r)-(p==q==r)
    else:a=3
    print(f"Case #{i}: "+['equilateral','isosceles','scalene','invalid!'][a]);i+=1