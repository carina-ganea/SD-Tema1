import random
Max = 1000000
n = 10000
f = open('test2.in', 'w')
f.write(str(n) + '\n')
for i in range(n):
    f.write(str(random.choice(range(Max))) + ' ')
