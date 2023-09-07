def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for index in range(k):
            for index in range(length):
                
                if index == 0:
                    firstnum = nums[0] 
                if index == length-1:
                    nums[index] = firstnum
                else:
                    nums[index] = nums[index+1]
            print(nums)
nums = [1,2,3,4,5,6,7]
k  =  3
rotate(nums,k=3)