class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        left = 0
        right = 0
        for n in nums:
            total += n
        for i, val in enumerate(nums):
            if i>0:
                left += nums[i-1]
                right = total-nums[i]-left
                if left == right:
                    return i
            if i==0:
                right = total - nums[0]
                if right != 0:
                    continue
                else:
                    return 0
        return -1

if __name__ == '__main__':
    sol = Solution()
    input = [1, 7, 3, 6, 5, 6]
    res = sol.pivotIndex(input)
    print(res)