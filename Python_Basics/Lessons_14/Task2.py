"""
�������� ��������� ����������� � ������ ���������� ����������� "�����" � "�������" � ������� �����������.
"""
def decorate(func):
    def wrapper():
        x = input("������� ����������")

        func()
        print(x)
    return wrapper

@decorate
def eat():
    print("���� ���")
eat()    