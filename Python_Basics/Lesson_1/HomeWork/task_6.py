USD, EUR = float(input()), float(input())
amount = lambda _USD=0.014, _EUR=0.84, quantity=1: round((quantity / _USD) / _EUR, 2)
print(amount(USD, EUR))
