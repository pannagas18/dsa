# WRONG; IT'S MAX JUMP SO JUMP VALUE CAN BE LESS THAN THE MAX JUMP VALUE THAT IS GIVEN IN THE LIST

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [1]

current_index = 0
while True:
    current_index += nums[current_index]
    print(nums[current_index])
    if current_index >= len(nums)-1 or nums[current_index] == 0:
        break
if current_index == len(nums)-1:
    print(True)
else: print(False)
