
def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_val = 0
    max_i = -2
    for i, val in enumerate(nums):
        if val >= max_val:
            max_val = val
            max_i = i
    for i, val in enumerate(nums):
        if max_val < val*2 and i != max_i:
            return -1
    return max_i


if __name__ == '__main__':
    #sol = Solution()
    input = [0, 0, 2, 3]
    input = [0, 0, 3, 2]
    input = [0, 0, 0, 1]
    res = dominantIndex(input)
    print res