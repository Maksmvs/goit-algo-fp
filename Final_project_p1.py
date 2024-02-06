class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    prev_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node


def insertion_sort_linked_list(head, ascending=True):
    if head is None:
        return None

    sorted_head = None
    current = head

    while current is not None:
        next_node = current.next
        if ascending:
            sorted_head = sorted_insert_ascending(sorted_head, current)
        else:
            sorted_head = sorted_insert_descending(sorted_head, current)
        current = next_node

    return sorted_head


def sorted_insert_ascending(sorted_head, new_node):
    if sorted_head is None or sorted_head.value >= new_node.value:
        new_node.next = sorted_head
        sorted_head = new_node
    else:
        current = sorted_head
        while current.next is not None and current.next.value < new_node.value:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    return sorted_head

def sorted_insert_descending(sorted_head, new_node):
    if sorted_head is None or sorted_head.value <= new_node.value:
        new_node.next = sorted_head
        sorted_head = new_node
    else:
        current = sorted_head
        while current.next is not None and current.next.value > new_node.value:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    return sorted_head


def merge_sorted_lists(head1, head2):
    dummy_node = Node(0)
    tail = dummy_node

    while True:
        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break

        if head1.value <= head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    return dummy_node.next


head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)

reversed_head1 = reverse_linked_list(head1)

sorted_head2 = insertion_sort_linked_list(head2, ascending=False)

merged_head = merge_sorted_lists(reversed_head1, sorted_head2)

current_node = merged_head
while current_node is not None:
    print(current_node.value, end=" -> ")
    current_node = current_node.next

