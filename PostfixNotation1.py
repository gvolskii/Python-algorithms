def postfix(string):
    numbers = Stack()
    for element in string.split():
        if element.isdigit():
            numbers.push(int(element))
        else:
            if element == '+':
                result = numbers.pop() + numbers.pop()
                numbers.push(result)
            elif element == '*': 
                result = numbers.pop() * numbers.pop()
                numbers.push(result)
            elif element == '=':
                return numbers.pop()
