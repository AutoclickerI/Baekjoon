for i in[*open(0)][:-1]:l,w,h,v=map(int,i.split());print(l or v//w//h,w or v//l//h,h or v//l//w,v or l*w*h)