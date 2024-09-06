inpu = input('Input: ')
vocals = ['a', 'e', 'i', 'o', 'u']
out = ''

for char in inpu:
    if char.lower() in vocals:
        continue
    out += char

print(f'Output: {out}')
