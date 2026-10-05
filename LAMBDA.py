multiply = lambda x: x*2
print(multiply(2))

Add =lambda x,y: x+y
print(Add(1,2))

check = lambda i: i in "python"
print(check('z'))

prices = ['$12.50','$9.90','$100.00']

math =list( map(lambda p : float(p.strip('$')),prices))
print(math)
#OR
math =list( map(lambda p : float(p.replace('$','')),prices))
print(math)

prices = ['$12.50','$9.90','$100.00']
p = '$12.50'
print(float(p.strip('$')))


prices = [120,30,300,80]
math= list(filter(lambda p: p >= 100 , prices))
print(math)

student = [['Maria', 85],['Kumar',90],['Max',60]]

math = list(filter(lambda row: row[1] > 70,student))
print(math)

import math
student = [['Maria', 85],['Kumar',90],['Max',60]]
math = list(filter(lambda row: row[0].startswith('M'),student))
print(math)


