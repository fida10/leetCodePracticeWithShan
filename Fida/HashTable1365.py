class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = [];

        for num in nums:
            sortedNums.append(num);
        sortedNums.sort();

        lesserThan = {};

        for i in range(len(nums)):
            if (sortedNums[i] not in lesserThan):
                lesserThan[sortedNums[i]] = i;

        for i in range(len(nums)):
            nums[i] = lesserThan[nums[i]];

        return nums;