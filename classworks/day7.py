items=["milk", "bread", "eggs"]
#function for adding one element.
def add_item():
    items.append("biscuit")
    print(items)
#function for removing last element.
def remove_item():
    items.pop()
    print(items)
add_item()
remove_item()
#lamda for printing element as Item:<item>
item=lambda x: print("item :",x)
for x in items:
    item(x)
#total number of character
def sum_characters(item, index=0):
    if index == len(item):
        return 0
    return len(item[index]) + sum_characters(item, index + 1)
print(sum_characters(items))