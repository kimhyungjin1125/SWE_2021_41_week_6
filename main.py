from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for idx1 in range(len(nums)-1):
        for idx2 in range(idx1+1, len(nums)):
            if nums[idx1] + nums[idx2] == target:
                print(f"[{idx1}, {idx2}]")
                break 
    return