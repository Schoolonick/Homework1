num: int = input()
print(sum(list(map(int, [num[0], num[len(num) // 2], num[-1]]))))
