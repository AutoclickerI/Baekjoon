import re
for i in[*open(0)][1:]:print(re.match('[A-F]?A+F+C+[A-F]?$\n',i)and'Infected!'or'Good')