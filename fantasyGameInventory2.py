stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = {'gold coin': 5, 'dagger': 1, 'ruby': 3}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item, amount in addedItems.items():
        inventory.setdefault(item, 0)
        inventory[item] += amount


displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)
