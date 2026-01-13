roll1=["Smruti", 27, 155.1, 60.5,"Black","Bhubaneswar"]
#size of a list
print(f'There are {len(roll1)} elements in the list')
#access an element with its index
print(f"Smruti's favorite color is {roll1[4]}")
print(f"Smruti's height is {roll1[2]} cms")
print(roll1[-1])
#slicing
print(roll1[0:2])
print(roll1[4:])
#iterating
for i in roll1:
    print(i)
for i in range(4):
    print(roll1[i])

#concatenation  
roll1add=["B+", 91381937481]
print(roll1+roll1add)
roll1.extend(roll1add)
print(roll1)

nest=[["Smruti",27,"Pink"],["Sukanya",28,"Blue"],["Minion",10,"Yellow"]]
print(f'The favorite color of Minion is {nest[2][2]}')
print(f'Smruti is {nest[0][1]} years old')
print(f'Name of the second student is {nest[1][0]}')
