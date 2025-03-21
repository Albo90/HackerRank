import os


def timeInWords(h, m):
    d = {0: "o' clock", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
         9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen",
         17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 21: "twenty one", 22: "twenty two",
         23: "twenty three", 24: "twenty four", 25: "twenty five", 26: "twenty six",
         27: "twenty seven", 28: "twenty eight", 29: "twenty nine", 30: "half"}
    hour = d[h]
    is_less = False
    if m > 30:
        is_less = True
        m = 60 - m
    minute = d[m]
    if is_less:
        hour = d[h + 1]
        s = f"{minute} minutes to {hour}"
        if m == 15:
            s = f"{minute} to {hour}"
        if m == 1:
            s = f"{minute} minute to {hour}"
    else:
        s = f"{minute} minutes past {hour}"
        if m in [15, 30]:
            s = f"{minute} past {hour}"
        if m == 1:
            s = f"{minute} minute past {hour}"
        if m == 0:
            s = f"{hour} o' clock"
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
