# input: input.txt
# part 1: How many measurements are larger than the previous measurement?
# part 2: Same as 1 but with three-measurement sums

import numpy as np

measurements=np.loadtxt('input.txt')

def run(part):
    if part==1:
        arr=measurements
    else:
        arr=np.convolve(measurements, np.ones(3), mode='valid')
    d=np.diff(arr)
    n=np.shape(np.where(d>0))[1]
    with open('output.txt', 'a') as f:
        f.write('Part {}: n={} \n'.format(part, n))

if __name__=='__main__':
    run(1)
    run(2)
