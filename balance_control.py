from classes import Stack


def balance_control(brackets):
    ex = Stack()
    for i in brackets:
        if i in '([{':
            ex.push(i)
        else:
            if not ex.is_empty() and ex.peek() == {')': '(', ']': '[', '}': '{'}[i]:
                ex.pop()
            else:
                return False
    return True
