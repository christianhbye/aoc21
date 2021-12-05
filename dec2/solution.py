import numpy as np

def run(part, pos, aim, ops):
    with open('input.txt', 'r') as f:
        for l in f: 
            d=l.split(' ')
            op=ops[d[0]]
            factor=int(d[1].split('\n')[0])   
            tup=np.array(op)*factor
            if part==1:
                pos+=tup
            elif part==2:
                pos[0]+=tup[0]
                aim+=tup[1]
                pos[1]+=tup[0]*aim
    return pos

if __name__=='__main__':
    ops={'forward': (1, 0), 'down': (0, 1), 'up': (0, -1)}
    for i in range(1, 3):
        with open('output.txt', 'a+') as f:
            f.write('Part {}: \n'.format(i))
            pos_out=run(i, np.zeros(2), 0, ops)
            f.write(str(pos_out))
            f.write('\n {} \n'.format(np.product(pos_out)))
