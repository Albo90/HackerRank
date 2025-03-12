def merge_the_tools(string, k):
    for i in range(k, len(string) + 1, k):
        sub = string[i - k:i]
        lst = []
        for j in sub:
            if not j in lst:
                lst.append(j)
        print("".join(lst))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)