def rotate_array(nums: list[int], k: int) -> None:
    """将数组向右旋转k步
    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> rotate_array(a, 3)
    >>> a
    [5, 6, 7, 1, 2, 3, 4]
    >>> b = [1, 2, 3, 4, 5, 6, 7]
    >>> rotate_array(b, 10)
    >>> b
    [5, 6, 7, 1, 2, 3, 4]
    """
    n = len(nums)
    k %= n  # 处理k > n的情况

    # 定义类似上题的函数作为辅助
    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    reverse(0, n - 1)   # 反转整个数组      ->  [7, 6, 5, 4, 3, 2, 1]
    reverse(0, k - 1)   # 反转前k个元素     ->  [5, 6, 7, 4, 3, 2, 1]
    reverse(k, n - 1)   # 反转后n-k个元素   ->  [5, 6, 7, 1, 2, 3, 4]

def stair_ways(n):
    """
    Yield all the ways to climb a set of n stairs taking
    1 or 2 steps at a time.

    >>> list(stair_ways(0))
    [[]]
    >>> s_w = stair_ways(4)
    >>> sorted([next(s_w) for _ in range(5)])
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
    >>> list(s_w) # Ensure you're not yielding extra
    []
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        yield []
    elif n == 1:
        yield [1]
    else:
        for way in stair_ways(n - 1):
            yield [1] + way
        for way in stair_ways(n - 2):
            yield [2] + way

ways = stair_ways(4)
print(next(ways))
print(next(ways))
print(next(ways))
print(next(ways))
print(next(ways))
print(next(ways))