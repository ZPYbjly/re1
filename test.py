def test(nums): 
        i = nums[0]
        j = 0
        k = 0
        flag = [] 
        arrays = []
        for num in nums:
            arrays.append(num)
        for index,num in enumerate(arrays):
            if i == num:
                j = j+1
                if j>2:
                  flag.append(index)
                       
            else:
                i = num
                j = 1

        for index in flag:
            del nums[index-k]
            k = k+1

        print(nums)
        return len(nums) - k
nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
test(nums)