from math import floor
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_pointer = 0
        end_pointer = len(nums) -1
        while start_pointer <= end_pointer:
            cur_pointer = start_pointer + floor((end_pointer-start_pointer)/2)
            if nums[cur_pointer] < target:
                start_pointer = cur_pointer + 1
            elif nums[cur_pointer] > target:
                end_pointer = cur_pointer -1
            else:
                return cur_pointer
        return -1