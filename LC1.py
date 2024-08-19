# the purpose of this code is to loop through a list of numbers and add its initial value to preceeding value THAT is already stored in the new list then append the value to the list

nums = [1, 2, 3, 4, 5]
answer = []

# need to loop through the range of the set
for i in range(len(nums)): # nums = 1,2,3,4,5 take len so 5, range 0-4
    counter = 0            # initalized counter to 0
    for j in range(i + 1): # index + 1 , j loops through 
        counter += nums[j] # counter += retrieve element in j index of nums 
    answer.append(counter) # append counter value to answer list 

print(answer)
