item = input('Чего ? :').lower()
answer = ''
if item == 'продукты':
    price = int(input('Дэнэг у тя ваабще сколька будет, А ? : '))
    if price < 100:
        answer = 'Хоч пирожки ??? :)'
    elif price > 100 and price < 500:
        answer = 'Давай тогда уж орехи в чоколаде ?'
    else:
        answer = 'Фруктов ?'
else:
    answer = 'Вам вообще не к нам, хоз.товары воооооООООН ТАМ !'

print(answer)
