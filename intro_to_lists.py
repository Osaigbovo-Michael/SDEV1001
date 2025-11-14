groceries = ["apples", "bananas", "carrots", "dates", "eggs", "flour", "grapes"]
print('Ourer grocery list contains:', groceries)
print('First item:', groceries[0])
print('Second item:', groceries[-1])

groceries[0] = "avocados"
groceries[2] = "cucumbers"
print('Updated grocery list contains:', groceries)

print(groceries[0:3])
print(groceries[3:])
print(groceries[:4])

print('The length of the grocery list is:')
print(len(groceries))