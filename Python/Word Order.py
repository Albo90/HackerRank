from collections import OrderedDict
n = int(input())
dct = OrderedDict()
for _ in range(n):
    key = input()
    value = dct.get(key) if dct.get(key) else 0
    dct[key] = value+1
print(len(dct.keys()))
res = ""
for key, val in dct.items():
    res+=" "+str(val)
print(res.strip())