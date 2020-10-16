fruits = ["Apple","Banana","Pineapple","Melon"]
fruits.append("kiwi")
print(fruits)

fruits.insert(0,"Orange")
print(fruits)

fruits.insert(33,"Peach")
print(fruits)

fruits.remove("Melon")
print(fruits)

# fruits.remove("Pear") # not in the list
# print(fruits)

fruits.pop(3)
print(fruits)

fruits[2] = "Strawberry"
print(fruits)
