import numpy as np

nums=np.loadtxt('input.txt', delimiter=',', max_rows=1)
boards=np.loadtxt('input.txt', skiprows=2).reshape(-1, 5, 5)
won_boards=[]
won_nums=[]
checked=np.isin(boards, nums[:5]).astype(int)

def bingo(check_arr, current_num):
    """
    Assumes check_arr is (N, 5, 5)-arr where N=number of boards
    """
    for i, checked_board in enumerate(check_arr):
        if i in won_boards:
            continue
        elif 5 in checked_board.sum(axis=0) or 5 in checked_board.sum(axis=1)
        or 5 == np.diag(checked_board).sum():
            won_boards.append(i)
            won_nums.append(current_num)
        else:
            continue

current_idx=4

while current_idx<len(nums):
    current_num=nums[current_idx]
    checked[np.isin(boards, current_num)]=1
    bingo(checked, current_num)
    if len(won_boards)==len(boards):
        break
    else:
        current_idx+=1
        continue

def get_score(win_number):
    """
    Get score for the [win_number]th board to win
    """
    board_no=won_boards[win_number]
    fullboard=boards[board_no]



unchecked=boards[x][uncheck_idx]
score=unchecked.sum()*nextnum
with open('output.txt', 'a+') as f:
    f.write('Part 1: {:d} \n'.format(int(score)))
