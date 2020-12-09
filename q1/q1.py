import numpy as np

# Easy N^2 solution

if __name__ == '__main__':
    in_arr = open("input.txt", "r+")
    A = in_arr.readlines()
    for i in range(len(A)):
        A[i] = int(A[i].rstrip('\n'))
    
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == 2020:
                print("%d * %d == %d"  % (A[i], A[j], A[i]*A[j]))