numbers = input('ведите все оценки студента через пробел ').split()
amount_fives = numbers.count('5')
print((amount_fives/len(numbers)*100))