import inflect
p = inflect.engine()
names = []

while True:
    try:
        name = input('Name: ').strip()
        names.append(name)
    except EOFError:
        break

formatted_names = p.join(names)
print(f"Adieu, adieu, to {formatted_names}")
