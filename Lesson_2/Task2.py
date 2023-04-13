final_list = [] 
for x in range(1):
    list = input("input list: ").split(' ')
    for elements in list:
        if list.count(elements) > 1:
            final_list.append(elements)
print(set(final_list))