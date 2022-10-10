#Danny Radosevich
#COSC1101
#Lists extras

#range
print("Range")
nums = list(range(0,10))
print(nums)

#simple stats
print("stats")
nums = [23,51,12,53,73,34,15]
print(min(nums))
print(max(nums))
print(sum(nums))

#list comp
print("list comp")
squares = [value**2 for value in range(1,11)]
print(squares)

#slices
print("slices")
nums = [2,5,1,3,9,6,0,8,7]
print(nums[:3])
print(nums[4:])
print(nums[-2:])

#copyin a list
print("copying")
nums_two = nums
nums_two.append(13)
print(nums)
nums_three = nums[:]
nums_three.append(42)
print(nums)
print(nums_three)