import math
for i in[*open(0)][2::2]:n=math.lcm(*map(int,i.split()));print([n,'More than a billion.'][n>1e9])