N,H,S=map(int,input().split())
*f,=map(int,input().split())
fibot=(N/2,S/N)
inc_M=min((S/N)/(N/2),(H-S/N)/(N/2))
inc_m=-inc_M
def get_area(inc):
    area=0
    for idx,i in enumerate(f):
        area+=((fibot[1]+(fibot[0]-idx)*inc)+(fibot[1]+(fibot[0]-idx-1)*inc))*i
    return area/2
print(min(get_area(inc_M),get_area(inc_m)))