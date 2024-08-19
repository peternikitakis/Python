# the purpose of this code is to loop through a list of numbers and add its initial value to preceeding value THAT is already stored in the new list then append the value to the list

nums = [1, 2, 3, 4, 5]
answer = []

# need to loop through the range of the set
for i in range(len(nums)): # nums = 1,2,3,4,5 take len so 5, range 0-4
    counter = 0 
    for j in range(i + 1):
        counter += nums[j]
    answer.append(counter)


print(answer)
