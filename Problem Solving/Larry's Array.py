import math
import os
import random
import re
import sys


#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    length = len(A) - 1
    while True:
        index = -1
        for idx in range(0, length):
            if idx > 0 and A[idx - 1] > A[idx + 1]:
                index = idx - 1
                break
            if A[idx] > A[idx + 1]:
                index = idx
                break
        if index == -1:
            return "YES"
        if index == len(A) - 2:
            return "NO"
        A[index], A[index + 1], A[index + 2] = A[index + 1], A[index + 2], A[index]
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
