arrays = [7,8,9,3,4,5]
list_h = sorted(arrays,reverse = True)
print(list_h)
for index,num in enumerate(list_h):
            if num<index:
                
                h_index = index-1
                print(h_index)
                break
        