    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        returnValue =[]
        sort = sorted(nums)
        dict = {}
        
        
        for j, k in enumerate(sort):
            if k not in dict:
                dict[k] = j
        for j in nums:
            returnValue.append(dict[j])
        return returnValue
    