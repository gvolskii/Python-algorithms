def palindrome(string):
    symbols = Deque()
    for symbol in string.lower():
        if symbol != ' ':
            symbols.addTail(symbol)
    while symbols.size() > 1:
        if symbols.removeFront() != symbols.removeTail():
            return False
    return True
