cars = ['honda', 'toyota', 'nissan', 'lincoln']

# pop out luxury cars of the list and print
luxury_car = cars.pop(3)
print(luxury_car.title())

# change all japanese cars to german
cars[0] = 'volkswagen'
cars[1] = 'audi'
cars[2] = 'bmw'
print(cars)

# add another german luxury car
cars.append("Mercedes")
print(cars)

# remove any unreliable cars
cars.remove('volkswagen')
print(cars)

# sort list
cars.sort()
print(cars)

# reverse list
cars.sort(reverse = True)
print(cars)

# capitalizing all words in the list
new_list = []
for car in cars:
 new_list.append(car.title())
print(new_list)

# print a message explaining how many elements are in the list
number_of_cars = len(new_list)
print(f"There are {number_of_cars} in the list")

# empty the list
del new_list[0]
del new_list[1]
del new_list[0]

print(new_list)

# now add american cars
new_list.insert(0, "chevrolet")
new_list.insert(1, "dodge")
new_list.insert(2, "ford")
print(new_list)

# capitlize all elements
capitalize_list = []
for i in new_list:
    capitalize_list.append(i.title())
print(capitalize_list)

        
