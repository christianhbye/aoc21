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

tot=np.sum(split_digits(report), axis=0)[::-1]
gamma=np.sum(2**(np.argwhere(tot>n/2)[:, 0]))
epsilon=np.sum(2**(np.argwhere(tot<n/2)[:, 0]))
print(gamma*epsilon)
