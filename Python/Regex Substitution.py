import re
n = int(input())
for _ in range(n):
    str_1 = input()
    while re.search(r"( &{2} )", str_1):
        str_1 = re.sub(r"( &{2} )", " and ", str_1)
    while re.search(r"( \|{2} )", str_1):
        str_1 = re.sub(r"( \|{2} )", " or ", str_1)
    print(str_1)