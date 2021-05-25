

end = " "
class meetings:

    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


def maxMeeting(l, n):

    ans = []


    l.sort(key=lambda x: x.end)

    ans.append(l[0].pos)

    time_limit = l[0].end


    arr = []
    arr1 = []
    for i in range(1, n):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end

    for i in ans:
        print(i + 1)
        arr.append(i+1)
    # print(arr1.count(arr))


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
n = 6
li = []

for i in range(n):
    li.append(meetings(s[i], f[i], i))

maxMeeting(li, n)