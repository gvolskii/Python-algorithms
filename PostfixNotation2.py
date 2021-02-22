def postfix(stack):
    numbers = Stack()
    element = stack.pop()
    while element:
        if type(element) == int:
            numbers.push(element)
        else:
            if element == '+':
                result = numbers.pop() + numbers.pop()
                numbers.push(result)
            elif element == '*': 
                result = numbers.pop() * numbers.pop()
                numbers.push(result)
            elif element == '=':
                return numbers.pop()
        element = stack.pop()
