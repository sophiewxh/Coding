"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def check_sum(nums, k):
    targets = []
    for i in nums:
        diff = k - i
        if i in targets:
            return True
        else:
            targets.append(diff)
    return False


if __name__ == '__main__':
    a = [10, 15, 3, 7]
    k = 17

    print(check_sum(a, k))
