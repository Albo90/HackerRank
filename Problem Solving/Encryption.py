import math
import os

def encryption(s):
    lgt = len(s)
    f_num = math.sqrt(lgt)
    rows = math.floor(f_num)
    col = math.ceil(f_num)
    if (col * rows) < lgt:
        rows = col
    lst = []
    res = []
    for _ in range(rows):
        if len(s) < col:
            lst.append(s)
        else:
            lst.append(s[0:col])
            print(s[0:col])
            s = s[col::]
    for i in range(col):
        res.append("")
        for item in lst:
            if len(item) > i:
                res[i] = res[i] + item[i]
    s_1 = " ".join(res)
    return s_1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
