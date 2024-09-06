camel_str = input("camelCase: ")
result = ''
for char in camel_str:
    if not char.islower():
        result += '_'
    result += char.lower()
print(f'snake_case: {result}')

