# Variables and Data Types
# Inlike C and C++, in Python we do not specify the data type for the variable

name = "Harish Aale" #String
age = 23 #Int
gpa = 3.8 #Float
gpas = [3.4, 3.0, 3.8, 4] #List, by default mutable.
city, province, country = "Kathmandu", "Bagmati", "Nepal"
graduated = False #Boolean o or 1
achievements = None #Null
parents = ("Gita Aale", "Ramu Aale") #Tuple aka Immutable List


# Since we have not defined types for the variable
# Let's see type inference in action
type(name)
type(age)
type(gpa)

# No of semester Harish Aale has passed ?
# len() function prints the length of a list
len(gpas)

# What is the gpa obtained by Harish Aale in 3rd semester?
print(gpas[2])

# What is the gpa obtained by Harish Aale upto 3rd semester?

print(gpas[:3]) #or
print(gpas[0:3])

# To Print whole list
gpas[:] #or
gpas[0:len(gpas)]
gpas[::]

# Print odd semester marks of Harish Aale
gpas[0:4:2] # Prints from zeroth index to third index with step size 2. 

# Modify Items in a List
gpas[0] = 3.0
gpas[-1] = 4

# We cannot modify a tuple. Why? Because tuple is immutable.
gpas[0] = "Sita Aale" # throws error

