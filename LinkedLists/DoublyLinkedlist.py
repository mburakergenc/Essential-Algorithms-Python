class Node:
    """
    Doubly Linked List Algorithms
    """
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# Create Nodes
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("new node")
node5 = Node("add at beginning")
node6 = Node("add at end")

# Link the Nodes in both ways
node1.next = node2
node2.next = node3

node3.prev = node2
node2.prev = node1


def insertCell(afterMe, newCell):
    """
    Insert a cell after another cell
    :param afterMe:
    :param newCell:
    :return:
    """
    newCell.next = afterMe.next
    afterMe.next = newCell

    newCell.next.prev = afterMe.next
    newCell.prev = afterMe

insertCell(node2, node4)


def iterate(top):
    """
    Iterate over the Nodes
    :param top:
    :return:
    """
    while top is not None:
        print(top.data)
        top = top.next

    # End While
# End iterate

# iterate(node1)


def findCell(top, target):
    """
    Find the cell given as target
    :param top:
    :param target:
    :return top or None:
    """
    while top is not None:
        print(top.data + '--' + str(target))
        if top.data == target:
            return top
        top = top.next
    # End while
    # If we get this far, the target is not in the list
    return None
# End findcell

# findCell(node1, "3")


def finCellBefore(top, target):
    """
    findCellBefore algorithm modified to use a sentinel
    :param top:
    :param target:
    :return the cell before teh cell that contains the target cell:
    """
    while top.next is not None:
        if top.next.data == target:
            return top
        top = top.next
    # End while
    # If we get this far, the target is not in the list
    return None
# End findCellBefore


def addAtBeginning(top, newCell):
    """
    Add a new cell at the beginning of the linked list (Time complexity O(1))
    :param top:
    :param newCell:
    :return:
    """
    newCell.next = top.next
    top.next = newCell

    newCell.next.prev = top.next
    newCell.prev = top

# End addAtBeginning

# addAtBeginning(node1, node5)
# iterate(node1)


def addAtEnd(top, newCell):
    """
    Add a new cell at the end of the linked list (Time complexity O(N))
    :param top:
    :param newCell:
    :return:
    """
    while top.next is not None:
        top = top.next
    # End while

    # Add a new cell at the end
    top.next = newCell
    newCell.next = None

    newCell.prev = top
# End addAtEnd

addAtEnd(node1, node6)
iterate(node1)


def destroyList(top):
    """
    Destroy the Linked List
    :param top:
    :return:
    """
    while top:
        # Set all the links to None
        top.next = None

        # Free top if Garbage Collection is not used
        # free(top)

        # Move to the next cell
        top = top.next

# End destroyList
destroyList(node1)
