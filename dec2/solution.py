import numpy as np

pos=np.array([0, 0])
ops={'forward': (1, 0), 'down': (0, 1), 'up': (0, -1)}
with open('input.txt', 'r') as f:
    for i, l in enumerate(f): 
        d=l.split(' ')
        op=ops[d[0]]
        factor=int(d[1].split('\n')[0])   
        pos+=np.array(op)*factor  
print(pos)
print(np.product(pos))
