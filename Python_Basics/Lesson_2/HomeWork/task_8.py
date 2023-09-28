string = input()
for value in (("ический", "."), ("ическая", ".")):
    string = string.replace(*value)
print(string)
