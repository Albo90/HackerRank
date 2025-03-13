import math
import os
import random
import re
import sys

# Complete the time_delta function below.
from dateutil.parser import parse
def time_delta(t1, t2):
    datetime_object_1 = parse(t1)
    datetime_object_2 = parse(t2)
    t1 = datetime_object_1.timestamp()
    t2 = datetime_object_2.timestamp()
    res = t1-t2
    return str(abs(int(res)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
