add_new = input('Хотите добавить нового преподавателя? 1-если ,2-если хотите завершить программу ')
final_list = []
while add_new !='2':
    surname = input('ведите фамилию преподавтателя: ')
    job = input('Введите должность преподавателя: ')
    amount = input('ведите общие число студентов').split(',')
    final_list.append ([surname , job,amount])
    add_new= input('Хотите добавить нового преподавателя ? 1 - да 2 -нет')
    print(final_list)