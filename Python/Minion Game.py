def minion_game(string):
    cons_len = 0
    wows_len = 0
    res = "Draw"
    lt = len(string)
    for item in range(lt):
        s = string[item::]
        ln = len(s)
        if s[0].upper() in "aeiou".upper():
            wows_len+=ln
        else:
            cons_len+=ln
    res_cond = wows_len-cons_len
    if res_cond == 0:
        print(res)
        return res
    if res_cond > 0:
        res = f"Kevin {wows_len}"
        print(res)
        return res
    res = f"Stuart {cons_len}"
    print(res)
    return res

if __name__ == '__main__':
    s = input()
    minion_game(s)