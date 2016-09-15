class Node(object):
    """
    Singly Linked List Algorithms
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


# Create Nodes
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("New Cell")

# Link the Nodes
node1.next = node2
node2.next = node3


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


def findCellBefore(top, target):
    """
    Find the cell before the cell that contains the target cell
    :param top:
    :param target:
    :return the cell before teh cell that contains the target cell:
    """
    # If the list is emtpy target values is not present. Check top.next safely
    if top is None:
        return None

    # Search for the target value
    while top.next is not None:
        if top.next.data == target:
            return top
        top = top.next
    # End while
    # If we get this far, the target is not in the list
    return None
# End findcellbefore

# findCellBefore(node1, "3")

def findCellBefore(top, target):
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
# End addAtBeginning

# addAtBeginning(node1, node4)
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
# End addAtEnd

# addAtEnd(node1, node4)
# iterate(node1)


def insertCell(afterMe, newCell):
    """
    Insert a new cell after a specific cell (Time complexity 0(1))
    :param afterMe:
    :param newCell:
    :return:
    """
    newCell.next = afterMe.next
    afterMe.next = newCell
# End insertCell


def deleteAfter(afterMe):
    """
    Delete the cell after the cell afterMe
    :param afterMe:
    :return:
    """
    afterMe.next = afterMe.next.next
    # If you use a language that doesn't use Garbage Collection(like C++), perform an extra work.
    # free(target_Cell)
# End deleteAfter
#deleteAfter(node2)
#iterate(node1)


def deleteAfter1(afterMe):
    """
    deleteAfter function if you use a language that doens't support Garbage Collection.
    :param afterMe:
    :return:
    """
    tergetCell = afterMe.next
    afterMe.next = afterMe.next.next
    # free(targetCell)
# End deleteAfter1


def destroyList(top):
    while top:
        # Set all the links to None
        top.next = None

        # Free top if Garbage Collection is not used
        # free(top)

        # Move to the next cell
        top = top.next

# End destroyList
destroyList(node1)
iterate(node1)