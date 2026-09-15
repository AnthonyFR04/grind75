class Solution:
    def search(self, nums: List[int], target: int) -> int:
        cur_pointer = len(nums) // 2
        start_pointer = 0
        end_pointer = len(nums)
        while True:
            if nums[cur_pointer] < target:
                start_pointer = cur_pointer
                cur_pointer = (end_pointer + cur_pointer) // 2
            elif nums[cur_pointer] > target:
                end_pointer = cur_pointer
                cur_pointer //= 2
            else:
                return cur_pointer
            if (cur_pointer == end_pointer) or (cur_pointer == start_pointer):
                break
        return -1