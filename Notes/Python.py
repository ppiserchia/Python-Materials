# Python lesson 1
# Integers, Strings, Lists, and Indexing
numbers = "3, 5, 6, 8"
print(numbers[0])
print(numbers[-1])

# Strings
name = "Pasquale"
print(name[1])
print("My favorite letter is " , name[0])


# Integers
weight = 60.3
print("My weight is " , weight , " kg")

# Basic Arithmetic Operations
# Addition, Subtraction, Multiplication, Division
sum = 3 + 7
print(sum)

sub = 5 - 2
print(sub)

mul = 4 * 6
print(mul)

div = 12/4
print(div)

# We can also make arithemetic operations consequently. 

ab = 5
ab += 3 
ab += 4
print (ab)

bc = 10
bc -= 2
bc -= 3
print(bc)

# We can also check the type of item we're typing, by using the type() function.
name5 = 'Hello'
age = 15
print(type(name5))
print(type(age))

# Lists and Indexables Integers and Strings
# In Lists, we can store multiple items in a single variable.
# Lists are defined by square brackets [] and items are separated by commas.
vegetables = ["carrot", "broccoli", "spinach", "cauliflower", "bellpepper", "lettuce", "cabbage"]

# If we want to print a specific item from the list, we can index them, by using [] and inserting the number, as the position the item has in the list.
print(vegetables[0])
print("My favourite vegetables are " , vegetables[1] , vegetables [2], vegetables[4])
print("I have " , len(vegetables) , " vegetables in my list")
print(vegetables[0][2])
print(vegetables[3][2])
print(vegetables[5][3])

# We can also use negative indexing to access items from the end of the list.
print(vegetables[-1]) # it will print the last item in the list, which is "cabbage"
print(vegetables[-3]) # it will print the third last item in the list, which is "bellpepper"

# We can index also Strings!
word = "Python"
print(word[0])  # it will print the first letter "P"

# The strings in the list can also be indexed, for that you use a second []
names = ['Curie', 'Dawring', 'Turing']
print("my favourite letter is: ", names[2][0])  # it will print the first letter of the third element in the list.
print("My favourite letters are: ", names[0][1] , names[1][3] , names[2][5])

# Nested lists
veg = [["lettuce", "lettuce", "peppers", "courgette"], ["lettuce", "lettuce", "peppers", "potatoes"], ["lettuce", "coriander", "peppers", "courgette"]]
# How can we index "coriander"?
# We use two sets of brackets: the first one to select the list, the second one to select the item in that list.
print("the next ingredient is: ", veg[2][1]) # in this case, we select the third list, and then the second item.

# We can add or remove items from a list.

items = ["apple", "banana", 11]
items.pop(2) # with .pop() we remove an item from the list.
print(items)

items.append("peach") # with.append() we add an item from the list.
print(items)

items.insert(0, "pear") # with .insert() we can insert an item in a specific position we declare in first place.
print(items)

# What if we want a range os values from an indexable object?
# Then we use the ":" inside the square brackets and give the range
# The range will go from the first value and up tobut NOT including the second value
binomial_name = "Drosophilia melanogaster"
group = binomial_name[0:10]
print(group)

species = binomial_name[0:11] # I selected to index up to position 11 to include the first word, Drosophilia.
print(species)

quote = "To be, or not to be, that is the question."
verb_Auxiliar = quote[0:5]
print(verb_Auxiliar)

# The same is happening with nested lists:
chemical_Components = [["Hydrogen", "O"], ["Carbon", "C"], ["Nitrogen", "N"], ["Oxygen", "O"]]
frog_withD = chemical_Components[0][0][2:6] # Here I indexed the first list, then the first item, and selected the words in the range from 2 to 6.
print(frog_withD)

# Functions: max(), round(), type()
# Functions are pieces of code that allow you to do specific tasks. They can take inputs, called arguments, and return outputs.

# Max() function returns the largest item in an iterable or the largest of two or more arguments.
nums = [3, 9, 23, 56, 81]
largest_number = max(nums) # this will show the largest number in the list, which is 81.
print(largest_number)   