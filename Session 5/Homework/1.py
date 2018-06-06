inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seasheel', 'strange berry', 'lint']

for k, v in inventory.items():
    print (k, v)

backpack = inventory['backpack']
backpack.remove('dagger')
print(backpack)

inventory['gold'] += 50
print(inventory['gold'])
