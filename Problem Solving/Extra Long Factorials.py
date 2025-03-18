import math
import os
import random
import re
import sys


#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    res = 1
    for item in range(n, 1, -1):
        res = res * item
    print(res)


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
