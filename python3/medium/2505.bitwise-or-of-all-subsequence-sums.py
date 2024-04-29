#
# @lc app=leetcode id=2505 lang=python3
#
# [2505] Bitwise OR of All Subsequence Sums
#

# @lc code=start
class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        counter = []
        while nums:
            sum = 0
            tmp = []
            while nums:
                cur = nums.pop()
                sum += cur % 2
                cur //= 2
                if cur:
                    tmp.append(cur)
            counter.append(sum)
            nums = tmp
        n = len(counter)
        carry = 0
        ans = 0
        for i in range(n):
            counter[i] = int(counter[i]) + carry
            if counter[i] > 0:
                ans += 1 << i
            carry = counter[i] // 2
        while carry:
            ans += 1 << n
            n += 1
            carry //= 2
        return ans
        


# @lc code=end

