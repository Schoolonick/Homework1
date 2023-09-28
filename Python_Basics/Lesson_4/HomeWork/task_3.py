login = input()
list = ['=', '?', '^', '$', '№', '@', '_']
for n, letter in enumerate(login):
    if letter in list:
        print("Error letter:", letter, n)
