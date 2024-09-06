import sys
try:
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    file, extention = sys.argv[1].split('.')
    if extention != 'py':
        sys.exit('Not a Python file')

    with open(sys.argv[1]) as f:
        lines = 0
        inside_docstring = False
        for line in f.readlines():
            stripped_line = line.strip()

            if not stripped_line:
                continue
            if stripped_line.startswith(('"""', "'''")):
                if stripped_line.endswith(('"""', "'''")) and len(stripped_line) > 3:
                    continue 
                inside_docstring = not inside_docstring
                continue
            if inside_docstring:
                continue
            if stripped_line.startswith('#'):
                continue

            lines += 1
        print(lines)


except FileNotFoundError:
    sys.exit('File does not exist')

