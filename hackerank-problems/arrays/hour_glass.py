"""
    Given a  6 x 6 2D Array, :

    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0

    An hourglass in A is a subset of values with indices 
    falling in this pattern in arr's graphical representation:

    a b c
      d
    e f g

    There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. 
    Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. 
    The array will always be 6 x 6.
    
    Example
    arr =
    -9 -9 -9  1 1 1 
    0 -9  0  4 3 2
    -9 -9 -9  1 2 3
    0  0  8  6 6 0
    0  0  0 -2 0 0
    0  0  1  2 4 0

    The 16  hourglass sums are:

    -63, -34, -9, 12, 
    -10,   0, 28, 23, 
    -27, -11, -2, 10, 
    9,  17, 25, 18

    The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:
    0 4 3
      1
    8 6 6

"""

def hourglass_sum(arr):
    sum_all = None
    # can this be reduced to o(n) ?
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] \
            + arr[i+1][j+1] \
            + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            
            try:
                if total > sum_all: sum_all=total
            except TypeError:
                sum_all=total #
                
    return sum_all
