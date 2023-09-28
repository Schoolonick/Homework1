n = int(input())
last_digit = n % 10
if last_digit % 2 == 0:  # Проверяем, что последняя цифра четная
    for sum_of_digits in range(1, n):  # Проверяем, что сумма всех цифр числа кратна трем
        if sum_of_digits % 3 == 0:
            print(f"Число {n} делится на 6")
else:
    print(f"Число {n} не делится на 6")
