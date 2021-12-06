import numpy as np

nums=np.loadtxt('input.txt', delimiter=',', max_rows=1)
boards=np.loadtxt('input.txt', skiprows=2).reshape(-1, 5, 5)

checked=np.isin(boards, nums[:5]).astype(int)

def bingo(check_arr):
    """
    Assumes check_arr is (N, 5, 5)-arr where N=number of boards
    """
    for i, checked_board in enumerate(check_arr):
        if 5 in checked_board.sum(axis=0) or 5 in checked_board.sum(axis=1) or 5 == np.diag(checked_board).sum():
            return i
        else:
            continue
    return np.nan

for i in range(len(nums)-5):
    nextnum=nums[5+i]
    checked[np.isin(boards, nextnum)]=1
    x=bingo(checked)
    if np.isnan(x):
        continue
    else:
        uncheck_idx=np.logical_not(checked[x])
        unchecked=boards[x][uncheck_idx]
        score=unchecked.sum()*nextnum
        with open('output.txt', 'a+') as f:
            f.write('Part 1: {:d} \n'.format(int(score)))
        break
