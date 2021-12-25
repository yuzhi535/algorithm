''' 最大子段和 '''


def largeSum(nums: list):
    ans, last = 0, 0
    for i in nums:
        if last >= 0:
            last += i
        else:
            last = i
        ans = max(ans, last)
    return ans


def subLargeSum(nums: list, l: int, r: int):
    if l == r:
        return nums[l] if nums[l] > 0 else 0
    mid = (l+r)//2
    lSum = subLargeSum(nums, l, mid)
    rSum = subLargeSum(nums, mid+1, r)
    s1, s2 = nums[mid], nums[mid+1]
    lefts, rights = 0, 0
    for i in range(mid-1, l-1, -1):
        lefts += nums[i]
        s1 = max(s1, lefts)
    for i in range(mid+2, r+1, 1):
        rights += nums[i]
        s2 = max(s2, rights)
    s = s1+s2
    if s > lSum and s > rSum:
        return s
    elif lSum > rSum:
        return lSum
    return rSum


def test(nums, l, r):
    if l == r:
        return nums[l] if nums[l] > 0 else 0
    mid = (l+r)//2
    lSum = test(nums, l, mid)
    rSum = test(nums, mid+1, r)
    s1, s2, lefts, rights = 0, 0, 0, 0
    for i in range(mid, l-1, -1):
        lefts += nums[i]
        s1 = max(s1, lefts)
    for i in range(mid+1, r+1, 1):
        rights += nums[i]
        s2 = max(s2, rights)
    s = s1+s2
    if s > lSum and s > rSum:
        return s
    elif lSum > rSum:
        return lSum
    return rSum


nums = [3,-1,-2,-3,3]

print(largeSum(nums))
print(subLargeSum(nums, 0, len(nums)-1))
print(test(nums, 0, len(nums)-1))
