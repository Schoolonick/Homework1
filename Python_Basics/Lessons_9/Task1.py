"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""


def newfunc(n):
    print("Сириус -")
    print(input("Имя:"))
    print(input("Группа:"))
    n = int(input("Число студентов в группе:"))
    i = 0
    while i < n:
        i+=1
        newfunc(n)
print("Готово! Заберите бейджики")w