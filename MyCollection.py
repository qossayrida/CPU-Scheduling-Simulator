import matplotlib.pyplot as plt

class Process:
    def __init__(self, name, arrival_time, burst_time, priority, comeback_time):
        # Initialize a Process object with various attributes
        self.name = name  # Name of the process
        self.arrival_time = arrival_time  # Time when the process arrives
        self.burst_time = burst_time  # Time required by the process to complete
        self.priority = priority  # Priority of the process
        self.comeback_time = comeback_time  # Time for the process to comeback (if applicable)
        # Initialize attributes to track the progress and scheduling of the process
        self.remaining_burst_time = burst_time  # Remaining burst time
        self.remaining_priority = priority  # Remaining priority level
        self.total_ready_queue_time = 0  # Total time spent in the ready queue
        self.total_wait_queue_time = 0  # Total time spent in the wait queue
        self.ready_queue_time = 0  # Time spent in the ready queue during a specific period
        self.wait_queue_time = 0  # Time spent in the wait queue during a specific period
        self.CPU_time = 0  # Time spent executing on the CPU
        self.has_started = False  # Flag to check if process execution has started

def draw(processes, times, title, size):
    # Function to draw a Gantt chart for process scheduling
    # Create combinations of process, duration, and start time
    combinations = [(processes[i], times[i + 1] - times[i], times[i]) for i in range(len(processes))]
    # Sort combinations by process name and start times
    combinations.sort(key=lambda x: (x[0], x[2]))

    # Define a color map for different processes
    color_map = plt.get_cmap('tab10')

    # Plot Gantt chart bars
    fig, ax = plt.subplots(figsize=(17,7), dpi=300)
    for index, (process, duration, start) in enumerate(combinations):
        # Assume the process name ends with a number and assign a color
        process_color = color_map(int(process[-1]) % 10)
        ax.barh(process, duration, left=start, color=process_color)
        # Add a vertical line at the end of each task
        ax.axvline(x=start + duration, linestyle='--', linewidth=0.5)

    # Add labels and title to the plot
    ax.set_ylabel('Processes')
    ax.set_xlabel('Timeline')
    ax.set_xticks(times)  # Set x-axis ticks as the specified times

    # Rotate x-tick labels for better readability
    ax.set_xticklabels(times, fontsize=size, rotation='vertical')

    ax.set_title(title)
    plt.tight_layout()  # Adjust layout for a neat presentation
    plt.show()  # Display the plot

def fcfs_scheduling(process_list, total_time):
    # Initialize the simulation variables
    time = 0  # Current time in the simulation
    processes = []  # List to store the order of processes execution
    times = []  # List to store the corresponding times at which processes start execution
    ready_queue = []  # Queue for processes that are ready to be executed
    waiting_queue = {}  # Dictionary to store processes that are waiting and their comeback times
    current_process = None  # The current process being executed

    # Main loop to simulate each time unit until total_time is reached
    while time < total_time:
        # Check each process in the process list to see if it has arrived and not started yet
        for process in process_list:
            if process.arrival_time <= time and not process.has_started:
                ready_queue.append(process)  # Add to the ready queue
                process.has_started = True  # Mark the process as started

        # Check the waiting queue to move processes back to the ready queue if their comeback time is reached
        for process, comeback_time in list(waiting_queue.items()):
            if comeback_time <= time:
                ready_queue.append(process)
                del waiting_queue[process]

        # Check if the current process is done or if there is no current process, then pick the next process
        if ready_queue and (not current_process or current_process.remaining_burst_time == 0):
            if current_process:
                # Reset the current process' values and move it to the waiting queue
                current_process.remaining_burst_time = current_process.burst_time
                current_process.ready_queue_time = 0
                current_process.wait_queue_time = 0
                waiting_queue[current_process] = time + current_process.comeback_time
            # Take the next process from the ready queue
            current_process = ready_queue.pop(0)
            current_process.total_ready_queue_time += current_process.ready_queue_time
            current_process.total_wait_queue_time += current_process.wait_queue_time
            processes.append(current_process.name)
            times.append(time)

        # Increment the ready queue time for all processes in the ready queue
        for process in ready_queue:
            process.ready_queue_time += 1

        # Increment the wait queue time for all processes in the waiting queue
        for process in waiting_queue:
            process.wait_queue_time += 1

        # Update the CPU time and remaining burst time for the current process
        current_process.CPU_time += 1
        current_process.remaining_burst_time -= 1
        time += 1  # Increment the simulation time

    # Add the total time to the times list for the final timestamp
    times.append(total_time)

    # Print the process execution times and return the process order and their respective times
    print_times(process_list, processes, "First Come First Served")
    return processes, times


def sjf_scheduling(process_list, total_time):
    # Initialize the simulation variables
    time = 0  # Current time in the simulation
    processes = []  # List to store the order of process execution
    times = []  # List to store the corresponding times at which processes start execution
    ready_queue = []  # Queue for processes that are ready to be executed
    waiting_queue = {}  # Dictionary for processes in the waiting state with their comeback times
    current_process = None  # The current process being executed

    # Loop through each time unit until the total simulation time is reached
    while time < total_time:
        # Check for new arrivals and add them to the ready queue
        for p in process_list:
            if p.arrival_time <= time and not p.has_started:
                ready_queue.append(p)
                p.has_started = True

        # Move processes from the waiting queue back to the ready queue if their comeback time has passed
        for process, comeback_time in list(waiting_queue.items()):
            if comeback_time <= time:
                ready_queue.append(process)
                del waiting_queue[process]

        # Choose the next process to execute based on the SJF criteria
        if ready_queue and (not current_process or current_process.remaining_burst_time == 0):
            if current_process:
                # Reset current process' values and move it to the waiting queue
                current_process.remaining_burst_time = current_process.burst_time
                current_process.ready_queue_time = 0
                current_process.wait_queue_time = 0
                waiting_queue[current_process] = time + current_process.comeback_time
            # Select the process with the shortest burst time from the ready queue
            current_process = min(ready_queue, key=lambda p: p.burst_time)
            ready_queue.remove(current_process)
            current_process.total_ready_queue_time += current_process.ready_queue_time
            current_process.total_wait_queue_time += current_process.wait_queue_time
            processes.append(current_process.name)
            times.append(time)

        # Increment the waiting time for processes in the ready and waiting queues
        for process in ready_queue:
            process.ready_queue_time += 1
        for process in waiting_queue:
            process.wait_queue_time += 1

        # Update the CPU time and remaining burst time for the current process
        current_process.CPU_time += 1
        current_process.remaining_burst_time -= 1
        time += 1  # Increment the simulation time

    # Add the final timestamp to the times list
    times.append(total_time)

    # Print the process execution times and return the process order and their respective times
    print_times(process_list, processes, "Shortest Job First")
    return processes, times


def srtf_scheduling(process_list, total_time):
    # Initialize the simulation variables
    time = 0  # Current time in the simulation
    processes = []  # List to store the order of process execution
    times = []  # List to store the corresponding times at which processes start execution
    ready_queue = []  # Queue for processes that are ready to be executed
    waiting_queue = {}  # Dictionary for processes in the waiting state with their comeback times
    current_process = None  # The current process being executed

    while time < total_time:
        # Check for newly arrived processes
        for p in process_list:
            if p.arrival_time == time:
                ready_queue.append(p)
                p.has_started = True

        # Move processes from waiting queue to ready queue
        for process, comeback_time in list(waiting_queue.items()):
            if comeback_time == time:
                ready_queue.append(process)
                del waiting_queue[process]

        # Select process with shortest remaining time, different from last executed if possible
        if ready_queue:
            future_process = min(ready_queue, key=lambda p: p.remaining_burst_time)
            if not current_process or current_process.remaining_burst_time == 0:
                # Switch to the new process
                ready_queue.remove(future_process)
                if current_process:
                    current_process.remaining_burst_time=current_process.burst_time
                    current_process.ready_queue_time = 0
                    current_process.wait_queue_time = 0
                    waiting_queue[current_process] = time + current_process.comeback_time

                current_process = future_process
                current_process.total_ready_queue_time += current_process.ready_queue_time
                current_process.total_wait_queue_time += current_process.wait_queue_time
                processes.append(current_process.name)
                times.append(time)

            elif current_process.remaining_burst_time > future_process.remaining_burst_time:
                ready_queue.remove(future_process)
                ready_queue.append(current_process)
                current_process.ready_queue_time = 0
                current_process.wait_queue_time = 0
                current_process = future_process
                current_process.total_ready_queue_time += current_process.ready_queue_time
                current_process.total_wait_queue_time += current_process.wait_queue_time
                processes.append(current_process.name)
                times.append(time)


        for process in ready_queue:
            process.ready_queue_time += 1

        for process in waiting_queue:
            process.wait_queue_time += 1

        current_process.CPU_time += 1
        current_process.remaining_burst_time -= 1
        time += 1

    times.append(total_time)
    # Print the process execution times and return the process order and their respective times
    print_times(process_list, processes,"Shortest Remaining Time First")
    return processes, times

def round_robin_scheduling(process_list, total_time, q):
    # Initialize the simulation variables
    time = 0  # Current time in the simulation
    processes = []  # List to store the order of process execution
    times = []  # List to store the corresponding times at which processes start execution
    ready_queue = []  # Queue for processes that are ready to be executed
    waiting_queue = {}  # Dictionary for processes in the waiting state with their comeback times
    current_process = None  # The current process being executed
    time_quantum_remaining = 0  # Remaining time for the current time quantum

    # Loop through each time unit until the total simulation time is reached
    while time < total_time:
        # Check for new arrivals and add them to the ready queue
        for p in process_list:
            if p.arrival_time == time:
                ready_queue.append(p)
                p.has_started = True

        # Move processes from the waiting queue back to the ready queue if their comeback time has passed
        for process, comeback_time in list(waiting_queue.items()):
            if comeback_time == time:
                ready_queue.append(process)
                del waiting_queue[process]

        # Manage process execution based on the Round Robin algorithm
        if ready_queue and time_quantum_remaining == 0:
            # Check if the current process needs to be switched
            if current_process and current_process.remaining_burst_time != 0:
                # Put the current process back in the ready queue
                current_process.ready_queue_time = 0
                current_process.wait_queue_time = 0
                ready_queue.append(current_process)
            elif current_process and current_process.remaining_burst_time == 0:
                # Reset current process' values and move it to the waiting queue
                current_process.remaining_burst_time = current_process.burst_time
                current_process.ready_queue_time = 0
                current_process.wait_queue_time = 0
                waiting_queue[current_process] = time + current_process.comeback_time

            # Select the next process from the ready queue
            current_process = ready_queue.pop(0)
            current_process.total_ready_queue_time += current_process.ready_queue_time
            current_process.total_wait_queue_time += current_process.wait_queue_time
            processes.append(current_process.name)
            times.append(time)
            time_quantum_remaining = q  # Reset the time quantum

        elif current_process and current_process.remaining_burst_time == 0:
            # If the current process is completed within its quantum
            current_process.remaining_burst_time = current_process.burst_time
            current_process.ready_queue_time = 0
            current_process.wait_queue_time = 0
            waiting_queue[current_process] = time + current_process.comeback_time
            current_process = ready_queue.pop(0)
            current_process.total_ready_queue_time += current_process.ready_queue_time
            current_process.total_wait_queue_time += current_process.wait_queue_time
            processes.append(current_process.name)
            times.append(time)
            time_quantum_remaining = q

        # Increment the waiting time for processes in the ready and waiting queues
        for process in ready_queue:
            process.ready_queue_time += 1
        for process in waiting_queue:
            process.wait_queue_time += 1

        # Update the CPU time and remaining burst time for the current process
        current_process.CPU_time += 1
        current_process.remaining_burst_time -= 1
        time_quantum_remaining -= 1  # Decrement the time quantum
        time += 1  # Increment the simulation time

    # Add the final timestamp to the times list
    times.append(total_time)

    # Print the process execution times and return the process order and their respective times
    print_times(process_list, processes, "Round Robin Scheduling")
    return processes, times

def non_preemptive_priority_scheduling_with_aging(process_list, total_time):
    # Initialize the simulation variables
    time = 0  # Current time in the simulation
    current_process = None  # The current process being executed
    processes = []  # List to store the order of process execution
    times = []  # List to store the corresponding times at which processes start execution
    ready_queue = []  # Queue for processes that are ready to be executed
    waiting_queue = {}  # Dictionary for processes in the waiting state with their comeback times
    aging_tracker = {}  # Dictionary to track the aging of each process in the ready queue

    # Loop through each time unit until the total simulation time is reached
    while time < total_time:
        # Check for new arrivals and add them to the ready queue
        for p in process_list:
            if p.arrival_time <= time and not p.has_started:
                ready_queue.append(p)
                p.has_started = True
                aging_tracker[p.name] = 0  # Initialize aging time for the new process

        # Move processes from the waiting queue back to the ready queue if their comeback time has passed
        for process, comeback_time in list(waiting_queue.items()):
            if comeback_time <= time:
                ready_queue.append(process)
                del waiting_queue[process]

        # Select the process with the highest priority (lowest priority number)
        if not current_process or current_process.remaining_burst_time == 0:
            if current_process:
                # Reset current process' values and move it to the waiting queue
                current_process.remaining_priority = current_process.priority
                current_process.remaining_burst_time = current_process.burst_time
                current_process.ready_queue_time = 0
                current_process.wait_queue_time = 0
                waiting_queue[current_process] = time + current_process.comeback_time

            # Select the next process based on priority
            current_process = min(ready_queue, key=lambda p: p.remaining_priority)
            current_process.total_ready_queue_time += current_process.ready_queue_time
            current_process.total_wait_queue_time += current_process.wait_queue_time
            ready_queue.remove(current_process)
            processes.append(current_process.name)
            times.append(time)

        # Increment the waiting time for processes in the ready and waiting queues
        for process in ready_queue:
            process.ready_queue_time += 1
        for process in waiting_queue:
            process.wait_queue_time += 1

        # Update the CPU time and remaining burst time for the current process
        current_process.CPU_time += 1
        current_process.remaining_burst_time -= 1
        time += 1  # Increment the simulation time

        # Implement aging for the processes in the ready queue
        for p in ready_queue:
            aging_tracker[p.name] += 1
            # Check if aging should be applied (e.g., every 5 units of time)
            if aging_tracker[p.name] == 5:
                # Decrement the process's priority (increase its priority value) and reset aging time
                p.remaining_priority = max(p.remaining_priority - 1, 0)
                aging_tracker[p.name] = 0

    # Add the final timestamp to the times list
    times.append(total_time)

    # Print the process execution times and return the process order and their respective times
    print_times(process_list, processes, "Non Preemptive Priority Scheduling")
    return processes, times


def preemptive_priority_scheduling_with_aging(process_list, total_time):
    # Initialize the simulation variables
    time = 0  # Current time in the simulation
    current_process = None  # The current process being executed
    future_process = None  # The next process that could potentially be executed
    processes = []  # List to store the order of process execution
    times = []  # List to store the corresponding times at which processes start execution
    ready_queue = []  # Queue for processes that are ready to be executed
    waiting_queue = {}  # Dictionary for processes in the waiting state with their comeback times
    aging_tracker = {}  # Dictionary to track the aging of each process in the ready queue

    # Loop through each time unit until the total simulation time is reached
    while time < total_time:
        # Check for new arrivals and add them to the ready queue
        for p in process_list:
            if p.arrival_time <= time and not p.has_started:
                ready_queue.append(p)
                p.has_started = True
                aging_tracker[p.name] = 0  # Initialize aging time for the new process

        # Move processes from the waiting queue back to the ready queue if their comeback time has passed
        for process, comeback_time in list(waiting_queue.items()):
            if comeback_time <= time:
                aging_tracker[process.name] = 0
                ready_queue.append(process)
                del waiting_queue[process]

        # Select the process with the highest priority (lowest priority number)
        future_process = min(ready_queue, key=lambda p: p.remaining_priority)
        if not current_process or current_process.remaining_burst_time == 0:
            # Assign new process to the CPU if the current process is done or if there's no current process
            if current_process:
                # Reset current process' values and move it to the waiting queue
                current_process.remaining_priority = current_process.priority
                current_process.remaining_burst_time = current_process.burst_time
                current_process.ready_queue_time = 0
                current_process.wait_queue_time = 0
                waiting_queue[current_process] = time + current_process.comeback_time
            current_process = future_process
            current_process.total_ready_queue_time += current_process.ready_queue_time
            current_process.total_wait_queue_time += current_process.wait_queue_time
            ready_queue.remove(current_process)
            processes.append(current_process.name)
            times.append(time)

        elif current_process.remaining_priority > future_process.remaining_priority:
            # Preempt current process if a higher priority process is available
            aging_tracker[current_process.name] = 0
            current_process.ready_queue_time = 0
            current_process.wait_queue_time = 0
            ready_queue.append(current_process)
            current_process = future_process
            current_process.total_ready_queue_time += current_process.ready_queue_time
            current_process.total_wait_queue_time += current_process.wait_queue_time
            ready_queue.remove(current_process)
            processes.append(current_process.name)
            times.append(time)

        # Increment the waiting time for processes in the ready and waiting queues
        for process in ready_queue:
            process.ready_queue_time += 1
        for process in waiting_queue:
            process.wait_queue_time += 1

        # Update the CPU time and remaining burst time for the current process
        current_process.CPU_time += 1
        current_process.remaining_burst_time -= 1
        time += 1  # Increment the simulation time

        # Implement aging for the processes in the ready queue
        for p in ready_queue:
            aging_tracker[p.name] += 1
            # Check if aging should be applied (e.g., every 5 units of time)
            if aging_tracker[p.name] == 5:
                # Decrement the process's priority (increase its priority value) and reset aging time
                p.remaining_priority = max(p.remaining_priority - 1, 0)
                aging_tracker[p.name] = 0

    # Add the final timestamp to the times list
    times.append(total_time)

    # Print the process execution times and return the process order and their respective times
    print_times(process_list, processes, "Preemptive Priority Scheduling")
    return processes, times
def print_times(process_list, processes, title):
    # Initialize variables to calculate total wait time and total turnaround time
    total_wait_time = 0
    total_turnaround_time = 0
    number_of_process = 0  # To count the number of processes considered

    # Print the title of the scheduling algorithm used
    print(title, ":")

    # Loop through each process in the process list
    for process in process_list:
        # Check if the process was actually scheduled (exists in the processes list)
        if process.name in processes:
            number_of_process += 1  # Increment the process count
            # Accumulate the total wait time and turnaround time for each process
            total_wait_time += process.total_ready_queue_time
            total_turnaround_time += process.CPU_time + process.total_ready_queue_time + process.total_wait_queue_time

            # Print individual wait time and turnaround time for each process
            print(process.name, ":" "wait time=", process.total_ready_queue_time, "turnaround time=", process.CPU_time + process.total_ready_queue_time + process.total_wait_queue_time)

    # Calculate and print the average wait time and print the average turnaround time
    print("Avg wait time:", total_wait_time / float(number_of_process))
    print("Avg turnaround time:", total_turnaround_time / float(number_of_process), "\n\n")
