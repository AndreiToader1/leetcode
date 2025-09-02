from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        counter = 1
        for i in range (1, len(nums)):
            if nums[i] == candidate:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    candidate = nums[i]
                    counter = 1
        return candidate



if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    print(solution.majorityElement(nums))

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(solution.majorityElement(nums))

