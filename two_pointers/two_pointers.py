def two_pointers(array: list) -> list:
    n = len(nums)
    start, end = 0, n-1
    result = [0] * n
    idx = n-1

    while end > -1 and idx > -1:
        if abs(nums[start]) > abs(nums[end]):
            res[idx] = nums[start] ** 2
            start += 1
        else:
            res[idx] = nums[end] ** 2
            end -= 1
        idx -= 1

    return result
