import emoji
string = input('Input: ').strip()
print(f'Output: {emoji.emojize(string, language='alias')}')
