def BracketsBalanced(string):
    brackets = Stack()
    for symbol in string:
        if symbol == '(':
            brackets.push(symbol)
        if symbol == ')':
            if brackets.peek() != '(':
                return False
            brackets.pop()
    if brackets.size() > 0:
        return False
    return True
