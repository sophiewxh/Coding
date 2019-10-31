class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        l = len(digits)
        if l == 1:
            if digits[l - 1] == 9:
                result.append(1)
                result.append(0)
                return result
            else:
                result.append(digits[l - 1] + 1)
                return result
        else:
            if digits[l - 1] < 9:
                result = digits.copy()
                result[l - 1] += 1
                return result
            else:
                result = self.plusOne(digits[:l - 1]).copy()
                result.append(0)
                return result


if __name__ == '__main__':
    sol = Solution()
    input = [1, 9]
    res = sol.plusOne(input)
    print(res)