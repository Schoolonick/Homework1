login = input()
error = '=?*^$№@_'
list = []


for i in range(len(login)):
    if login[i] in error :
        list.append(login[i])

print(list)