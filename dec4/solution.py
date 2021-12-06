import numpy as np

nums=np.loadtxt('input.txt', delimiter=',', max_rows=1)
boards=np.loadtxt('input.txt', skiprows=2).reshape(-1, 5, 5)

#N=len(nums)-5
N=6
for i in range(5, N):
    print('\n---------------\n')
    checked=np.isin(boards, nums[:i])
    print(checked.shape)
    print(len(np.nonzero(checked)))
