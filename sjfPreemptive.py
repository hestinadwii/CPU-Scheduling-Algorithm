class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def shortest_remaining_time_first(processes):
    completed_processes = []
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    # loop until all processes are completed
    while len(processes) > 0:
        # find process with the smallest remaining_time and store its value
        min_time = min([p.remaining_time for p in processes])
        # select the process with the smallest remaining_time
        selected_process = [p for p in processes if p.remaining_time == min_time][0]

        # update waiting_time for all remaining processes
        for p in processes:
            if p != selected_process and p.arrival_time <= current_time:
                p.waiting_time += min_time

        # advance current_time by the smallest remaining_time
        current_time += min_time
        # decrement remaining_time of selected process
        selected_process.remaining_time -= min_time

        # if selected process is completed
        if selected_process.remaining_time == 0:
            # calculate turnaround time
            selected_process.turnaround_time = current_time - selected_process.arrival_time
            # calculate total waiting time
            total_waiting_time += selected_process.waiting_time
            # calculate total turnaround time
            total_turnaround_time += selected_process.turnaround_time
            # add completed process to completed_processes list
            completed_processes.append(selected_process)
            # remove completed process from processes list
            processes.remove(selected_process)

    avg_waiting_time = total_waiting_time / len(completed_processes)
    avg_turnaround_time = total_turnaround_time / len(completed_processes)

    return completed_processes, avg_waiting_time, avg_turnaround_time


