"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""
def check_pass():
    num_students = int(input("Введите число учеников: "))
    for i in range(num_students):
        score = int(input("Введите балл за финальный тест ученика: "))
        if score > 50:
            print(True)
        else:
            print(False)

check_pass()