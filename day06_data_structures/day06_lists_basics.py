print(" LIST BASICS ")

#List Sederhana
fruits= ["apple", "banana", "orange"]
print(fruits)

#Akses item
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Tambah dan hapus item
fruits.append("mango")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

# Looping dalam list
print("\nLooping")
for fruit in fruits:
    print("Fruit:", fruit)

# List of Numbers
numbers = [10, 20, 30, 40, 50]

print("\n BASIC OPERATIONS")
print("Total:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Length:", len(numbers))

# LIST COMPEREHENSION
print("\nLIST COMPEREHENSION")
squared = [n*n for n in numbers]
print("Squared numbers:", squared)