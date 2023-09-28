quantity = int(input())
amount = lambda RUB=1572, _quantity=100: RUB // _quantity if _quantity else 0
print(amount(_quantity=quantity))
