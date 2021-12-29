starts = [1, 4, 1, 8, 2, 3]
ends = [2, 5, 8, 14, 10, 6]
weights = [4, 3, 1, 5, 7, 8]


def weight(starts: list, ends: list, weights: list):
    items = [(starts[0], ends[0], weights[0])]
    for i in range(1, len(starts)):
        items.append((starts[i], ends[i], weights[i]))
    items.sort(key=lambda x: x[1])
    phead = [0 for i in range(len(items))]
    records = [0 for i in range(len(items))]

    for k in range(len(starts)):
        item = items[k][0]
        i, j, mid = 0, len(items), 0
        while i < j:
            mid = (i + j) // 2
            if items[mid][1] == item:
                break
            elif items[mid][1] > item:
                j = mid
            elif items[mid][1] < item:
                i = mid + 1
        if items[mid][1] > item:
            mid = -1
        phead[k] = mid

    dp = [0 for i in range(len(items) + 1)]
    for k in range(len(starts)):
        item = items[k][0]
        mid = phead[k]
        if mid == -1:
            if items[k][2] > (dp[k - 1] if k > 0 else 0):
                dp[k] = items[k][2]
                records[k] = 1
            else:
                dp[k] = dp[k - 1] if k > 0 else 0
                records[k] = 0
        else:
            if (dp[k - 1] if k > 0 else 0) < dp[mid] + items[k][2]:
                dp[k] = dp[mid] + items[k][2]
                records[k] = 1
            else:
                dp[k] = dp[k - 1] if k > 0 else 0
                records[k] = 0
    mmax = dp[len(items) - 1]
    i = len(items) - 1
    path = []
    while i >= 0:
        if records[i] == 1:
            path.append(i)
            i = phead[i]
        else:
            i -= 1
    path.reverse()
    for i in path:
        print(items[i], end=" ")
    print("\n", end="")
    return mmax


result = weight(starts, ends, weights)
print(result)
