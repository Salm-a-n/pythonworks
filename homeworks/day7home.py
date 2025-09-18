inventory=[]
#function for adding for adding item names.
def add_item(item):
    inventory.append(item)
# print(inventory)
# recursive function for counting .
def count_item(items):
    if not items:
        return 0
    else:
        return 1+count_item(items[1:])
# lambda function to print item in an oredr.
show_item=lambda item: print(f"Item in Stock: {item}")
# main function for adding ,calling other functionalities .
def main():
   add_item("dog food")
   add_item("cat toy")
   add_item("bird cage")
   add_item("fish tank")
   for item in inventory:
       show_item(item)
   print(f"the total number of item is {count_item(inventory)}")
main()
    