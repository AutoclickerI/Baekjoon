from decimal import*
getcontext().prec=999
for _ in[0]*int(input()):
    x_lb,y_lb,x_rt,y_rt=map(D:=Decimal,input().split())
    x1,y1,x2,y2,x3,y3=map(D,input().split())
    x2+=D('1E-100');y2+=D('1E-100')
    x3+=D('2E-100');y3+=D('2E-100')
    xylis=[[x1,y1],[x2,y2],[x3,y3]]
    ccw=lambda *l:sum(l[i][1]*l[i-1][0]-l[i][0]*l[i-1][1]for i in range(len(l)))/2
    AB=lambda x:(y2-y1)/(x2-x1)*(x-x1)+y1
    AB_1=lambda y:(x2-x1)/(y2-y1)*(y-y1)+x1
    BC=lambda x:(y3-y2)/(x3-x2)*(x-x2)+y2
    BC_1=lambda y:(x3-x2)/(y3-y2)*(y-y2)+x2
    CA=lambda x:(y3-y1)/(x3-x1)*(x-x1)+y1
    CA_1=lambda y:(x3-x1)/(y3-y1)*(y-y1)+x1
    cl1=lambda func,func_1:(3,func_1(y_lb),y_lb)if func(x_lb)<y_lb else(0,x_lb,func(x_lb))if y_lb<=func(x_lb)<=y_rt else(1,func_1(y_rt),y_rt)
    cl2=lambda func,func_1:(3,func_1(y_lb),y_lb)if func(x_rt)<y_lb else(2,x_rt,func(x_rt))if y_lb<=func(x_rt)<=y_rt else(1,func_1(y_rt),y_rt)
    A=[cl1(AB,AB_1),cl2(AB,AB_1)]
    B=[cl1(BC,BC_1),cl2(BC,BC_1)]
    C=[cl1(CA,CA_1),cl2(CA,CA_1)]
    ara=(x_rt-x_lb)*(y_rt-y_lb)
    def area(l,n):
        p,q=sorted(l);p3,p1,p2=p;q3,q1,q2=q;a=(ccw([q1,q2],[x_rt,y_lb],[x_rt,y_rt],[p1,p2])if q3==3 else ccw([q1,q2],[x_rt,y_rt],[x_lb,y_rt],[p1,p2]))if q3-p3==2 else(ccw([q1,q2],[x_lb,y_rt],[p1,p2])if q3==1 else ccw([q1,q2],[x_rt,y_rt],[p1,p2])if q3==2 else ccw([q1,q2],[x_rt,y_lb],[p1,p2])if p3==2 else ccw([q1,q2],[x_lb,y_lb],[p1,p2]))
        return ara-abs(a)if a*ccw([q1,q2],xylis[n],[p1,p2])>0 else abs(a)
    ans=area(A,2)+area(B,0)+area(C,1)+abs(ccw([x1,y1],[x2,y2],[x3,y3]))-ara
    if ccw([x1,y1],[x2,y2],[x3,y3])<0:ans=ara-ans
    print(f'{ans:.15f}')