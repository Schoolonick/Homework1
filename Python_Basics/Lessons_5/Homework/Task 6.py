list = []

while 1 :
    price = int(input())
    if price == 0: break
    list.append(price)

cheqe = sum(list)

if cheqe % 2 == 0:
    while cheqe % 2 == 0:
        cheqe = cheqe / 2
elif cheqe % 2 != 0:
    cheqe = cheqe/100*85
print('К оплате: ', cheqe)