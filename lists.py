#creating a list with 6 elements indexing from 0 to 5
roll1=["Smruti", 27, 155.1, 60.5,"Black","Bhubaneswar"]
#size of a list
print(f'There are {len(roll1)} elements in the list')
#access an element with its index
#to access the first element, index will always be 0
#to access the last element, index will always be -1 or len(listname)-1
print(f"Smruti's favorite color is {roll1[4]}")
print(f"Smruti's height is {roll1[2]} cms")
print(roll1[-1])
#slicing
#slicing is in the format listname[startIndex: endIndex +1]
#now if the end index is greater than the last index, then we leave it as empty
print(roll1[0:2])
print(roll1[4:])
#iterating using for loop directly will access the elements for me 1 by 1
for i in roll1:
    print(i)
 #iterating using for loop using range is for a particular length only and through its index
for i in range(4):
    print(roll1[i])

#concatenation  - means adding 2 or more lists
roll1add=["B+", 91381937481]
print(roll1+roll1add)

roll1.extend(roll1add)
print(roll1)

#one list inside another is known as nested list
#to access an element inside the nested list, first find the index of the outer list then the position within the inner list
nest=[["Smruti",27,"Pink"],["Sukanya",28,"Blue"],["Minion",10,"Yellow"]]
print(f'The favorite color of Minion is {nest[2][2]}')
print(f'Smruti is {nest[0][1]} years old')
print(f'Name of the second student is {nest[1][0]}')
