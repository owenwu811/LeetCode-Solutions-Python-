#we are given an input array, tasks, which contains the start and end times of n tasks. Your task is to find the minimum number of machines required to complete these n tasks

#input: Tasks = [(1, 7), (8, 13), (5, 6), (10, 14), (6, 7)]
#output: minimum machines required = 2

#input: Tasks = [(1, 7), (8, 9), (3, 6), (9, 14), (6, 7)]
#output: minimum machines required = 2 because machine 1: [(1, 7), (8, 9)] and machine 2: [(3, 6), (6, 7), (9, 14)]

#input: Tasks = [(5, 6), (5, 6), (5, 6), (5, 6), (6, 7)]
#output: minimum machines required = 4 because machine 1: [(5, 6), (6, 7)], machine 2: [(5, 6)]

#python3 solution (two heaps pattern):

#we use two heaps because we require efficient access to two quantities that are computed after sorting: the task with the earliest start time not yet scheduled and the machine whose currently scheduled workload is smaller aka ends first

#Why do we maintain the two heaps? the first heap stores the tasks to be scheduled such that the root of the heap will be the task with the earliest start time, and the second heap stores the list of machines such that the root of the heap will be the machine that will be free before all others - machine whose last task is smaller aka ends earliest
#next, iterate through input list to schedule each task on machines that aren't currently booked. So, For each task:

#1. check if there are any machines to use. If there are machines available to use, compare the end time of the machine whose workload ends the earliest with the start time of the current task. If the machine is free at the start time of the current task, we can use it. Therefore, we update the scheduled end time of this machine.
#2. if no available machines or machines in use when current task starts, we need a new machine, so we schedule the task on a new machine and add it to the list of machines, and also increment the count of machines used by 1.

#after processing all these tasks, we will know the minimum number of machines required


import heapq

def tasks(tasks_list):
  #add up the total # of machines for "optimal machines" task
  optimal_machines = 0
  #empty array to store tasks' finish times
  machines_available = []
  #converting list to set of "optimal_machines" to a heap
  heapq.heapify(tasks_list)
  while tasks_list: #loop through tasks input list
    #remove the task i with the earliest start time from tasks_list
    task = heapq.heappop(tasks_list)
    if machines_available and task[0] >= machines_available[0][0]:
      #top element is removed from "machines_available" array
      machine_in_use = heapq.heappop(machines_available)
      #schedule task on the current machine
      machine_in_use = (task[1], machine_in_use[1])
    else:
      #if there's a conflicting task, increment the counter for machines and store this task's end time on heap "machines_available"
      optimal_machines += 1
      machine_in_use = (task[1], optimal_machines)
    heapq.heappush(machines_available, machine_in_use)
  #return the total number of machines use by "tasks_list" tasks
  return optimal_machines


  
  


