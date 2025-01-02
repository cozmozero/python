def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        result = []

        for num in nums:
            if num != 0:
                result.append(num)

        zero_count = len(nums) - len(result)

        result.extend([0] * zero_count)

        for i in range(len(nums)):
            nums[i]=result[i]

        

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)