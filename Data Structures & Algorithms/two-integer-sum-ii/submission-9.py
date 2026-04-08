class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):  # Start j after i
                if numbers[i] + numbers[j] == target:
                    # Return indices with +1 for 1-indexed
                    return [i + 1, j + 1]