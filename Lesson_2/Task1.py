list = input("Enter your list: ").split(' ')
search_element = input("Enter element: ")
counter = 0
for element in list:
    if search_element == element:
        counter += 1
print(counter)