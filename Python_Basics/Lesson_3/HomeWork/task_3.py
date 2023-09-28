x, y, z = [int(input()) for n in range(3)]
amount = x + y + z
end = ''
if x < y < z:
    amount /= 2
elif x > y > z:
    amount /= 3

print(f"К оплате  {amount}")
