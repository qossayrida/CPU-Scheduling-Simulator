import MyCollection  # Presumably contains the process class and scheduling algorithms
import copy  # Used for creating deep copies of objects

# Define a list of processes with their attributes (name, arrival time, burst time, priority, comeback time)
process_list = [
    MyCollection.Process("Process 1", 0, 10, 0, 2),
    MyCollection.Process("Process 2", 1, 8, 0, 4),
    MyCollection.Process("Process 3", 3, 14, 0, 6),
    MyCollection.Process("Process 4", 4, 7, 0, 8),
    MyCollection.Process("Process 5", 6, 5, 0, 3),
    MyCollection.Process("Process 6", 7, 4, 0, 6),
    MyCollection.Process("Process 7", 8, 6, 0, 9)
]

# First Come First Served (FCFS) Scheduling
# Apply the FCFS scheduling algorithm to a deep copy of the process list and visualize the result
processes, times = MyCollection.fcfs_scheduling(copy.deepcopy(process_list), 200)
MyCollection.draw(processes, times, "First Come First Served", 10)

# Shortest Job First (SJF) Scheduling
# Apply the SJF scheduling algorithm to a deep copy of the process list and visualize the result
processes, times = MyCollection.sjf_scheduling(copy.deepcopy(process_list), 200)
MyCollection.draw(processes, times, "Shortest Job First", 10)

# Shortest Remaining Time First (SRTF) Scheduling
# Apply the SRTF scheduling algorithm to a deep copy of the process list and visualize the result
processes, times = MyCollection.srtf_scheduling(copy.deepcopy(process_list), 200)
MyCollection.draw(processes, times, "Shortest Remaining Time First", 8)

# Round Robin Scheduling
# Apply Round Robin scheduling with a time quantum of 5 to a deep copy of the process list and visualize the result
processes, times = MyCollection.round_robin_scheduling(copy.deepcopy(process_list), 200, 5)
MyCollection.draw(processes, times, "Round Robin Scheduling", 10)

# Non-Preemptive Priority Scheduling with Aging
# Apply non-preemptive priority scheduling with aging to a deep copy of the process list and visualize the result
processes, times = MyCollection.non_preemptive_priority_scheduling_with_aging(copy.deepcopy(process_list), 200)
MyCollection.draw(processes, times, "Non Preemptive Priority Scheduling", 10)

# Preemptive Priority Scheduling with Aging
# Apply preemptive priority scheduling with aging to a deep copy of the process list and visualize the result
processes, times = MyCollection.preemptive_priority_scheduling_with_aging(copy.deepcopy(process_list), 200)
MyCollection.draw(processes, times, "Preemptive Priority Scheduling", 10)

