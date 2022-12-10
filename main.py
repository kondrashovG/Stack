class Stack:

    def __init__(self: list):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

if __name__ == '__main__':
    bb1 = '(((([{}]))))'
    bb2 = '[([])((([[[]]])))]{()}'
    bb3 = '{{[()]}}'
    ub1 = '}{}'
    ub2 = '{{[(])]}}'
    ub3 = '[[{())}]'
    # b_dict = {')':'(',']':'[','}':'{'}
    ex = Stack()
    for i in bb1:
        print(i)
        if i in '([{':
            ex.push(i)
        else:
            # print({')':'(',']':'[','}':'{'}[i])
            # print(ex.peek())
            if ex.peek() == {')':'(',']':'[','}':'{'}[i]:
                print(ex.pop())
            else:
                print('Скобки не сбалансированы')
                break






