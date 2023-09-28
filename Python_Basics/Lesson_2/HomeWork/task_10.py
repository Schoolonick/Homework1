word = {
    '': ['-', ' ', '(', ')']
}
string = input()

for key, value in word.items():
    for sign in value:
        string = string.replace(sign, key)
    break
print(string)
