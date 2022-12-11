from balance_control import balance_control


if __name__ == '__main__':
    brackets = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    for j in brackets:
        print(j)
        if balance_control(j):
            print('Скобки сбалансированы')
        else:
            print('Скобки не сбалансированы')
