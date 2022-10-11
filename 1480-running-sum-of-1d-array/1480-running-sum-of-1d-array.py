class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = []
        cumm = 0
        for num in nums:
            rs.append(cumm + num)
            cumm = cumm + num
        return rs