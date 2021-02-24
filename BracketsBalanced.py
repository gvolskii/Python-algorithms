def BracketsBalanced(string):
    brackets = Stack()
    for symbol in string:
        if symbol == '(':
            brackets.push(symbol)
        if symbol == ')':
            if brackets.pop() != '(':
                return False
    return brackets.size() == 0
