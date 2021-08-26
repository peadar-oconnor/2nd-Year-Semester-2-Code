# Peadar O'Connor 117302273
import math


class SLLNode:
    """
    A node for use in the Singly linked list ADT.

    Can hold an element and the next node in the list.
    """
    def __init__(self, item, nextnode):
        self.element = item     #any object
        self.next = nextnode    #an SLLNode


class SLinkedList:
    """
    A Singly linked list made up of linked nodes.

    Each node is linked to the next one in the list in order.

    This SLL ADT is taken from CS2515:Algorithms and Data Structures I
    """
    def __init__(self):
        self.first = None
        self.size = 0

    def add_first(self, element):
        """ Add node to the start of the list """
        node = SLLNode(element, self.first)
        self.first = node
        self.size = self.size + 1

    def get_first(self):
        """ Return the first element of the list """
        if self.size == 0:
            return None
        return self.first.element

    def get_first_node(self):
        """ Return the first node of the list """
        if self.size == 0:
            return None
        return self.first

    def remove_first(self):
        """ Remove the first element of the list """
        if self.size == 0:
            return None
        item = self.first.element
        self.first = self.first.next
        self.size = self.size - 1
        return item

    def get_length(self):
        """ Return the length of the list. """
        length = 0
        current = self.get_first()
        while current:
            current = current.next
            length += 1
        return length


class Queue:
    """
    A queue using a python list, with internal wrap-around..

    Head and tail of the queue are maintained by internal pointers.
    When the list is full, a new bigger list is created.

    This queue ADT is taken from CS2515:Algorithms and Data Structures I
    """

    def __init__(self):
        self.body = [None] * 10
        self.head = 0  # index of first element, but 0 if empty
        self.tail = 0  # index of free cell for next element
        self.size = 0  # number of elements in the queue

    def __str__(self):
        output = '<-'
        i = self.head
        if self.head < self.tail:
            while i < self.tail:
                output = output + str(self.body[i]) + '-'
                i = i + 1
        else:
            while i < len(self.body):
                output = output + str(self.body[i]) + '-'
                i = i + 1
            i = 0
            while i < self.tail:
                output = output + str(self.body[i]) + '-'
                i = i + 1
        output = output + '<'
        output = output + '     ' + self.summary()
        return output

    def get_size(self):
        """ Return the internal size of the queue. """
        return sys.getsizeof(self.body)

    def summary(self):
        """ Return a string summary of the queue. """
        return ('Head:' + str(self.head)
                + '; tail:' + str(self.tail)
                + '; size:' + str(self.size))

    def grow(self):
        """ Grow the internal representation of the queue.

        This should not be called externally.
        """
        # print('growing')
        # print('Before growing:')
        # print(self)
        oldbody = self.body
        self.body = [None] * (2 * self.size)
        oldpos = self.head
        pos = 0
        if self.head < self.tail:  # data is not wrapped around in list
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos = pos + 1
                oldpos = oldpos + 1
        else:  # data is wrapped around
            while oldpos < len(oldbody):
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos = pos + 1
                oldpos = oldpos + 1
            oldpos = 0
            while oldpos <= self.tail:
                self.body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos = pos + 1
                oldpos = oldpos + 1
        self.head = 0
        self.tail = self.size

    def enqueue(self, item):
        """ Add an item to the queue.

        Args:
            item - (any type) to be added to the queue.
        """
        # An improved representation would use modular arithmetic
        if self.size == 0:
            self.body[0] = item  # assumes an empty queue has head at 0
            self.size = 1
            self.tail = 1
        else:
            self.body[self.tail] = item
            # print('self.tail =', self.tail, ': ', self.body[self.tail])
            self.size = self.size + 1
            if self.size == len(self.body):  # list is now full
                self.grow()  # so grow it ready for next enqueue
            elif self.tail == len(self.body) - 1:  # no room at end, but must be at front
                self.tail = 0
            else:
                self.tail = self.tail + 1
        # print(self)

    def dequeue(self):
        """ Return (and remove) the item in the queue for longest. """
        # An improved implementation would use modular arithmetic
        if self.size == 0:  # empty queue
            return None
        item = self.body[self.head]
        self.body[self.head] = None
        if self.size == 1:  # just removed last element, so rebalance
            self.head = 0
            self.tail = 0
            self.size = 0
        elif self.head == len(self.body) - 1:  # if head was the end of the list
            self.head = 0  # we must have wrapped round, so point to start
            self.size = self.size - 1
        else:
            self.head = self.head + 1  # just move the pointer on one cell
            self.size = self.size - 1
        # we haven't changed the tail, so nothing to do
        return item

    def length(self):
        """ Return the number of items in the queue. """
        return self.size

    def first(self):
        """ Return the first item in the queue. """
        return self.body[self.head]  # will return None if queue is empty


class Process:
    """
    A class for a memory-using process. It has an id and a set size
    for use in the memory allocation algorithm.
    """
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.access_bit = 1
        self.used_pages = None


class Block:
    """
    A class for a block in the memory. Each block has a number of pages
    assigned, and how big these pages are determine the total space allocated
    to the block.
    """
    def __init__(self, max_pages, page_size):
        self.max_pages = max_pages
        self.page_size = page_size
        self.remaining_pages = max_pages
        self.space = max_pages * self.page_size
        self.process_list = []


def firstFit(process, linked_list, queue):
    """
    Takes the first block from the linked list which is greater than or equal
    to the requested size. If it can't find one it calls on the second chance
    algorithm to free up some blocks until process can be added.
    """
    added = False
    current_node = linked_list.get_first_node()
    # iterates through list, either reaching the end or stopping if hitting the if statement
    while current_node is not None:
        current_block = current_node.element
        # if the process fits in the remaining space of a block
        if current_block.space >= process.size:
            # process list is used to find the process later
            current_block.process_list.append(process)
            print("Process with ID %i and size %i KB added to block with max pages of %i." % (process.id, process.size, current_block.max_pages))
            # math.ceil rounds the number up to see how many pages are needed to fit the process
            process.used_pages = math.ceil(process.size / current_block.page_size)
            print("-> Pages used by this process = %i." % process.used_pages)
            current_block.remaining_pages -= process.used_pages
            print("-> Pages remaining in this block = %i." % current_block.remaining_pages)
            current_block.space = (current_block.remaining_pages * current_block.page_size)
            # above line would not work correctly if there were no remaining pages (multiplying by 0)
            if current_block.remaining_pages == 0:
                current_block.space = 0
            added = True
            # second chance queue
            queue.enqueue(process)
            # stops iterating through list
            current_node = None
        else:
            current_node = current_node.next
    if not added:
        # if something can't be added and the second chance queue is empty then the process is too big
        if queue.length() == 0:
            print("Error: Process with ID %i and size %i KB is too large for any block and was not added." % (process.id, process.size))
        else:
            secondChance(queue, linked_list)
            # tries to add the process again, will recursively call until added
            firstFit(process, linked_list, queue)


def deAllocation(process, linked_list):
    """
    Process is found in the linked list and removed from the block.
    """
    current_node = linked_list.get_first_node()
    # iterates through list in same way as first fit
    while current_node is not None:
        current_block = current_node.element
        # finding the process in the list
        if process in current_block.process_list:
            print("Process with ID %i and size %i KB de-allocated." % (process.id, process.size))
            current_block.remaining_pages += process.used_pages
            print("-> Pages remaining in this block = %i." % current_block.remaining_pages)
            current_block.space = (current_block.remaining_pages * current_block.page_size)
            # process is still in second chance queue, so this tells the second chance that its done with
            process.access_bit = 0
            current_block.process_list.remove(process)
            current_node = None
        else:
            current_node = current_node.next


def secondChance(queue, linked_list):
    """
    Page replacement managed by a queue. Removes page from queue and checks
    access bit. If its 1, then its set to 0 and page is added back to the queue.
    If its 0, then the page is de-allocated form the linked list.
    """
    process = queue.dequeue()
    if process.access_bit == 0:
        deAllocation(process, linked_list)
    else:
        process.access_bit = 0
        print("Process with ID %i and size %i KB given second chance, added back to queue." % (process.id, process.size))
        queue.enqueue(process)


def simulation(ll_specs, processes_list):
    """
    Simulates all the algorithms working together. Creates a linked list of memory
    blocks using given values, and runs first fit using given processes.
    """
    sll = SLinkedList()
    queue = Queue()
    for tuple in ll_specs:
        i = 0
        # adds how many of each block wanted for the linked list
        while i < tuple[0]:
            # tuple[1] is how many pages per block, 4 is how many KB per page
            sll.add_first(Block(tuple[1], 4))
            i += 1

    for item in processes_list:
        firstFit(item, sll, queue)