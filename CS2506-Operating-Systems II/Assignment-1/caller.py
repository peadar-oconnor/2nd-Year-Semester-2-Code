from lab1 import *

a = Process("A", 500, 2)
b = Process("B", 900, 4, 480, 2000)
c = Process("C", 3000, 5)
#d = Process("D", 1000, 5, 500, 1000)
#e = Process("E", 600, 6)
#f = Process("F", 800, 6)

s = SchedulerRunner([a, b, c], 8, 10)
s.run()




'''
i = 0
a = [1,2,3]
while i < len(a):
    a.pop()
    print("pop")
'''
'''
current_level = item._process._priority - 1
                                    print(current_level)
                                    queue_list[current_level + 1].addToQueue(item._process)
                                    item._process = False
                                    blocked_queue_list.pop()
'''