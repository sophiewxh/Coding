"""
You have a lock in front of you with 4 circular wheels.
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible.
"""

class Solution:
    def openLock(self, deadends, target):


        start = "0000"
        digits = start
        if digits == target:
            return 0

        if int(digits[0]) != int(target[0]):









if __name__ == '__main__':
    sol = Solution()
    # example 1
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    a,b,c,d = "0202"
    print(b)
    print(c)