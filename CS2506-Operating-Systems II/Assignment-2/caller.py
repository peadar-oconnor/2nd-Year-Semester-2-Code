from lab2 import *

# specifications for creating the linked list; 48 blocks of 2 pages,
# 32 blocks of 4 pages etc. Order is backwards since linked list nodes are
# added to the front of the list.
ll_specs = [(12, 32), (16, 16), (20, 8), (32, 4), (48, 2)]

# creating all the processes
p1 = Process(1, 4)
p2 = Process(2, 4)
p3 = Process(3, 6)
p4 = Process(4, 8)
p5 = Process(5, 12)
p6 = Process(6, 2)
p7 = Process(7, 12)
p8 = Process(8, 16)
p9 = Process(9, 24)

p_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

# run sim
simulation(ll_specs, p_list)

print()
print("----- Second chance demonstration -----")
print()

p10 = Process(10, 128)
p11 = Process(11, 128)
p12 = Process(12, 128)
p13 = Process(13, 128)
p14 = Process(14, 128)
p15 = Process(15, 128)
p16 = Process(16, 128)
p17 = Process(17, 128)
p18 = Process(18, 128)
p19 = Process(19, 128)
p20 = Process(20, 128)
p21 = Process(21, 128)
p22 = Process(22, 128)
p23 = Process(23, 128)
p24 = Process(24, 128)

p_list2 = [p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24]

simulation(ll_specs, p_list2)

'''
def firstFit(process, linked_list, queue):
    """"""
    added = False
    current_block = linked_list.get_first()
    while current_block != None:
        if current_block.space > process.size:
            print("h")
            current_block.process_list.append(process)
            process.used_pages = math.ceil(process.size / current_block.page_size)
            current_block.remaining_pages -= process.used_pages
            current_block.space -= current_block.remaining_pages * current_block.page_size
            added = True
            queue.enqueue(process)
            current_block = None
        else:
            current_block = current_block.next
    if not added:
        secondChance(queue, linked_list)
        firstFit(process, linked_list, queue)
        

def deAllocation(process, linked_list):
    current_block = linked_list.get_first()
    while current_block:
        if process in current_block.process_list:
            current_block.remaining_pages += process.used_pages
            current_block.space -= (current_block.remaining_pages * current_block.page_size)
            process.access_bit = 0
            current_block.process_list.remove(process)
            current_block = None
        current_block = current_block.next
'''