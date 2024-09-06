item = input('Item: ')
item = item.lower()
dicti = {'apple' : 130,
         'avocado' : 50,
         'sweet cherries' : 100,
         'kiwifruit' : 90,
         'pear' : 100}
if item not in dicti:
    print('')
else:
    print(f'Calories: {dicti[item]}')
