def LinkedListSum(list_one, list_two):
    if (list_one.len() != list_two.len()) and (list_one.len() == 0):
        return
    list_sum = LinkedList()
    node_one = list_one.head
    node_two = list_two.head
    while node_one is not None:
        list_sum.add_in_tail(Node(node_one.value + node_two.value))
        node_one = node_one.next
        node_two = node_two.next
    return list_sum