# Peadar O'Connor 117302273

"""
Each process has a name, a duration in ms, a priority which denotes what level it gets
put into, when an IO operation would start in ms (defaults to 0 if there is no
IO operation), and the duration of said IO operation in ms (again, default value
of 0). prev_blocked is also provided for the class, but will never be set to
true unless done so in the scheduler, hence why its not inside __init__ attributes.
"""


class Process:
    def __init__(self, name, duration, priority, io_when=0, io_duration=0):
        self._name = name
        self._duration = duration
        self._priority = priority
        self._io_when = io_when
        self._io_duration = io_duration
        self._prev_blocked = False

    # declare property
    @property
    # getter
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority

    @property
    def io_when(self):
        return self._io_when

    @io_when.setter
    def io_when(self, io_when):
        self._io_when = io_when

    @property
    def io_duration(self):
        return self._io_duration

    @io_duration.setter
    def io_duration(self, io_duration):
        self._io_duration = io_duration

    '''
    string representation for testing
    '''

    def __str__(self):
        return "%i, %i, %i, %i, %s" % (self._duration, self._priority,
                                       self._io_when, self._io_duration, self._prev_blocked)


class ReadyQueue:
    def __init__(self, time_slice):
        self._time_slice = time_slice
        # always starts empty
        self._process_list = []

    @property
    def time_slice(self):
        return self._time_slice

    @time_slice.setter
    def time_slice(self, time_slice):
        self._time_slice = time_slice

    '''
    emptyCheck returns true if a queue is empty. this is used to  move on to the next
    queue in the scheduler
    '''

    def emptyCheck(self):
        if not self._process_list:
            return True
        return False

    '''
    addToQueue appends the process to the end of the process queue
    '''

    def addToQueue(self, process):
        self._process_list.append(process)

    '''
    removeFromQueue removes from the process queue
    '''

    def removeFromQueue(self):
        self._process_list.pop(0)

    '''
    nextUp returns the process at the end of the list. Used to modify process attributes
    '''

    def nextUp(self):
        return self._process_list[-1]

    def __str__(self):
        return "%i, %s" % (self._time_slice, self._process_list)


class BlockedQueue:
    def __init__(self, io_duration):
        self._io_duration = io_duration
        self._process = False

    @property
    def io_duration(self):
        return self._io_duration

    @io_duration.setter
    def io_duration(self, io_duration):
        self._io_duration = io_duration

    def __str__(self):
        return "%i, %s" % (self._io_duration, self._process_list)


class Scheduler:
    def __init__(self, levels, quantum):
        self._levels = levels
        self._quantum = quantum
        self._queues = []

    @property
    def levels(self):
        return self._levels

    @levels.setter
    def levels(self, levels):
        self._levels = levels

    @property
    def quantum(self):
        return self._quantum

    @quantum.setter
    def quantum(self, quantum):
        self._quantum = quantum

    '''
    schedulingAlgorithm implements the algorithm for feedback queue scheduling.
    The number of levels of the scheduler and all the processes (in a list) that need to be 
    scheduled are provided. These are used to lay out all the queues and fill them with 
    processes to be run.
    Firstly enough queues are made for all levels, then the processes provided are added to the
    queues. scheduler goes though each level starting at 0. If its empty it moves on to the next level.
    For each process in a level, the process runs for the queues timeslice. IO operations cause a process 
    to be removes from the ready queue and put into the blocked queue, where it will complete its IO 
    operation. When its completed it will return to the ready queue with a higher priority. 
    Assumption made: the last queue has no duration, processes run as long as they need to
    '''

    def schedulingAlgorithm(self, processes):
        levels = self._levels
        queue_list = []
        blocked_queue_list = []
        i = 0
        # creating all the queues
        while i < levels:
            # determining the allocated time slice for each queue
            time_slice = ((2 ** i) * self._quantum)
            queue = ReadyQueue(time_slice)
            queue_list.append(queue)
            i += 1

        # filling the queues with processes. correct queue is found using the processes priority
        for item in processes:
            queue_level = item.priority
            queue_list[queue_level].addToQueue(item)

        # goes through scheduler level by level, starting at priority 0
        current_level = 0
        # switch_level helps with switching levels after a blocked process comes back into a queue
        switch_level = False
        while current_level < levels:
            # if the queue isn't empty
            if queue_list[current_level].emptyCheck() is False:
                current_process = 0
                current_queue = queue_list[current_level]
                # if its not the last level of the scheduler
                if current_level != levels - 1:
                    # iterates through list of processes for this queue
                    while current_process < len(current_queue._process_list):
                        # shorthand variable for the selected process to work on
                        selected_process = current_queue._process_list[current_process]
                        # process runs
                        remaining_time = selected_process._duration - current_queue._time_slice
                        # checks if theres an IO operation coming up
                        if selected_process._io_when > 0:
                            # io_when shows how long until the IO op starts, time slice must also be taken from it
                            selected_process._io_when -= current_queue._time_slice
                        # if theres any blocked queues
                        if blocked_queue_list:
                            for item in blocked_queue_list:
                                item._process._io_duration -= current_queue._time_slice
                                # if the duration of the IO op is over
                                if item._process._io_duration <= 0:
                                    item._process._priority = current_level - 1
                                    switch_level = current_level - 1
                                    # adding back the blocked process to the correct level queue
                                    queue_list[current_level - 1].addToQueue(item._process)
                                    print("Process %s enters ready state, enters Level %i" %
                                          (item._process._name, current_level - 1))
                                    item._process = False
                                    blocked_queue_list.remove(item)
                        # if process still has time left in its duration
                        if remaining_time > 0:
                            # process runs for the duration of the queue time slice and moves on to next queue
                            selected_process._duration = remaining_time
                            # IO process present AND the point where an IO op would happen is reached AND not
                            # already blocked
                            if selected_process._io_duration > 0 and selected_process._io_when <= 0 and \
                                    selected_process._prev_blocked == False:
                                # accounts for if the time slice went too far past where the IO op should happen
                                selected_process._duration -= selected_process._io_when
                                print("Process %s runs, new time slice is %i" %
                                      (selected_process._name, selected_process._duration))
                                selected_process._prev_blocked = True
                                selected_process._priority -= 1
                                blocked_queue = BlockedQueue(selected_process._io_duration)
                                blocked_queue._process = selected_process
                                blocked_queue_list.append(blocked_queue)
                                print("Process %s enters blocked state" % selected_process._name)
                            else:
                                print("Process %s runs, new time slice is %i" %
                                      (selected_process._name, selected_process._duration))
                                queue_list[current_level + 1].addToQueue(selected_process)
                            current_queue.removeFromQueue()
                        # else means that the process has finished running and will be removed from the scheduler
                        else:
                            current_queue.removeFromQueue()
                            print("Process %s ends at Level %i" % (selected_process._name, current_level))
                # this else means its the last level of the scheduler, and processes will complete in their own time
                else:
                    # unblocked processes end
                    while current_process < len(current_queue._process_list):
                        print("Process %s ends at Level %i" %
                              (current_queue._process_list[current_process]._name, current_level))
                        current_queue.removeFromQueue()
                    # blocked processes end
                    if blocked_queue_list:
                        for item in blocked_queue_list:
                            print("Process %s unblocks, and ends at Level %i" %
                                  (item._process._name, current_level))
            if switch_level:
                # if it wasnt done this way then the level would get switched mid-queue and mess up calculations
                current_level = switch_level
                print("Process switches back to Level %i" % current_level)
                switch_level = False
            else:
                current_level += 1
                if current_level < levels:
                    print("Scheduler is now on Level %i" % current_level)
        self.idleProcess()

    def idleProcess(self):
        print("Idle process starts")


"""
SchedulerRunner runs the scheduling algorithm. It takes a list of processes which will
be parsed by the algorithm and sorted into queues, the number of levels in the scheduler, 
and the time quantum for the scheduler. 
"""


class SchedulerRunner:
    def __init__(self, processes, levels, quantum):
        self._levels = levels
        self._quantum = quantum
        self._processes = processes

    @property
    def processes(self):
        return self._processes

    @processes.setter
    def processes(self, processes):
        self._processes = processes

    @property
    def levels(self):
        return self._levels

    @levels.setter
    def levels(self, levels):
        self._levels = levels

    @property
    def quantum(self):
        return self._quantum

    @quantum.setter
    def quantum(self, quantum):
        self._quantum = quantum

    '''
    Creates a scheduler using the attributed provided for the SchedulerRunner class, 
    then runs the scheduling algorithm using the list of processes provided.
    '''
    def run(self):
        scheduler = Scheduler(self._levels, self._quantum)
        scheduler.schedulingAlgorithm(self._processes)
