import numpy as np

report=np.loadtxt('input.txt', dtype=int)
n=len(report)
m=np.max([len(str(report[i])) for i in range(n)])

def split_digits(arr):
    newarr=np.empty((n, m))
    for i, row in enumerate(arr):
        newrow=[int(d) for d in str(row)]
        x=m-len(newrow)
        newarr[i, :x]=np.zeros(x)  # pad 0s
        newarr[i, x:]=newrow
    return newarr

split_report=split_digits(report)

# part 1
tot=np.sum(split_report, axis=0)[::-1]
gamma=np.sum(2**(np.argwhere(tot>n/2)[:, 0]))
epsilon=np.sum(2**(np.argwhere(tot<n/2)[:, 0]))
with open('output.txt', 'a+') as f:
    f.write('Part 1: {:d}\n'.format(gamma*epsilon))

# part 2
def filter(arr, bit_no, rating='ogr'):
    n=len(arr)
    if n==1:
        return arr
    else:
        if rating=='ogr':
            condition=int(np.sum(arr[:, bit_no])>=n/2)
        elif rating=='csr':
            condition=int(np.sum(arr[:, bit_no])<n/2)
        ind=np.argwhere(arr[:, bit_no] == condition)[:, 0]
        return arr[ind]

x, y = 0, 0
for i in range(m):
    if i==0:
        ogarr=split_report
        csarr=split_report
    else:
        ogarr=x
        csarr=y
    x=filter(ogarr, i, rating='ogr')
    y=filter(csarr, i, rating='csr')

ogr=np.sum(2**np.argwhere(x[0, ::-1]==1)[:, 0])
csr=np.sum(2**np.argwhere(y[0, ::-1]==1)[:, 0])

with open('output.txt', 'a') as f:
    f.write('Part 2: {:d} \n'.format(ogr*csr))
    
