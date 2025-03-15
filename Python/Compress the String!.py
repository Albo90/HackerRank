import itertools

input = input()
lst = list(input)
res = []
for key, value in itertools.groupby(lst):
    item =(len(list(value)), int(key))
    res.append(item)
print(*res)