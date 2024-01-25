"""
������������ ���������, ������� ����� ���������� ����� (��� �����),
���� ��������� ������������� � ��������� �����(���� ��� �������� ����� ������� �������). ������� ������������
������ ������ ��� ����� ��� ���������. ����� ����� �� ������ �������
���� �  ���������������� ��� ���������, �������� ��� ���� ������ ��
������ � �������� �� ��� ������� � ����� ����������. ����� ��� �������� ������� ��������� ���� � ����� ��� ����� ������������ ��������
"""
def analyze_file(filename):
    word_count = {}
    max_count = 0
    max_words = []
    with open(filename, 'r') as file:
        for line in file:
            # ���������� ������ �� ����� � �������� �������� � ������ ����������
            words = line.lower().split()
            words = [w.strip('.,!?') for w in words]

            for word in words:
                # ������� ���������� ������������� ����
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

                # ���������� ������������� ���������� � ������ ����
                if word_count[word] > max_count:
                    max_count = word_count[word]
                    max_words = [word]
                elif word_count[word] == max_count:
                    max_words.append(word)

    return max_words
filename = input("������� ��� ����� ��� ���������: ")
most_common_words = analyze_file(filename)

if len(most_common_words) == 1:
    print("�������� ����� ������������� ����� � �����:", most_common_words[0])
else:
    print("�������� ����� ������������� ����� � �����:", ", ".join(most_common_words))