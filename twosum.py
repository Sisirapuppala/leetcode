//Bruteforce method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        a=list()
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j]==target:
                    a.append(i)
                    a.append(j)
        return(a)

        
