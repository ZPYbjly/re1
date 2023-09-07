def canJump(nums):        
        flag = False
        length = len(nums)
        cover = 0
        for index in range(length-1):
                cover = max(nums[index]+index,cover)
                print(cover)
        if cover >= length-1:
            flag = True
        return flag

nums = [2,3,5,1,4]
canJump(nums)