    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)
        return (bisect_left(sort, i) for i in nums)
        
        