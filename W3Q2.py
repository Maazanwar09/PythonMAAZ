nums =[]
for i in range(5):
 num = float(input(f"enter number {i+1}: "))
 nums.append(num)
 average = sum(nums)/5
print("average of number :", average)
