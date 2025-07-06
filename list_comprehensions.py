#List comprehensions are useful shorthands for such operations. They offer a shorter and more readable way to create lists with various settings using just a single line of code.

nums = [x for x in range(1,51)]
print(nums)

#ejercicio 2

nums = [x*2 for x in range(10)]
print(nums)


#ejercicio 3

tags = ["travel", "vacation", "journey"]

hashtags = ["#" + x for x in tags]
print(hashtags)



#ejercicio 4

users = ["Brandon", "Emma", "Brian", 
"Sophia", "Bella", "Ethan",
"Ava", "Benjamin", "Mia", "Chloe"]

group = [x for x in users if x[0] == "B"]
print(group)


#ejercicio 5

sports = ["Football", "Basketball", "Tennis", "Golf", "Volleyball"]
group = [x for x in sports if "ball" in x]


#ejercicio 6

words = ["tree", "button", "cat", "window", "defenestrate"]

# Use a list comprehension to filter out words longer than four letters
task = [x for x in words if len(x) > 4]
# Display the filtered list
print(task)

#ejercicio 7 error

coordinates = (4, 7, 9)
coordinates[1] = 5
print(coordinates)