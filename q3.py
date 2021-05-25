

end = " "


def longPalSubstr(str):

    n = len(str)

    maxlen = 1
    start = 0

    for i in range(n):
        for j in range(i, n):
            flag = 1

            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    flag = 0

            if (flag != 0 and (j - i + 1) > maxlen):
                start = i
                maxlen = j - i + 1

    print("longest palindrome is: ", end)
    SubString(str, start, start + maxlen - 1)
    return maxlen


def SubString(string, low, high):
    for i in range(low, high + 1):
        print(string[i], end)

string = "aaaabbaa"
print("Length is: ", longPalSubstr(string))