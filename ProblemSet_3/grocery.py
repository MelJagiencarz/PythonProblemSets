groceries = {}

try:
    while True:
        item = input()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1
except EOFError:
    result = ''
    for item, number in sorted(groceries.items()):
        item = item.upper()
        result += (f'{number} {item}\n')
    result
    print(result)
