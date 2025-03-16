from collections import defaultdict

if __name__ == '__main__':
    s = input()
    d = defaultdict(int)
    for i in s:
        d[i]+=1
    lst = d.items()
    lst = sorted(lst, key=lambda x :(-x[1], x[0]))
    for k in lst[0:3]:
        print(f"{k[0]} {k[1]}")
