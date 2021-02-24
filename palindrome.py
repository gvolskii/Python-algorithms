def palindrome(string):
    symbols = Deque()
    for symbol in string.lower():
        if symbol != ' ':
            symbols.addTail(symbol)
    while symbols.size():
        head, tail = symbols.removeFront(), symbols.removeTail()
        if head != tail and tail is not None:
            return False
    return True
