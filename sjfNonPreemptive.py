class sjfNonPreemptive:
    def __init__(self, processes):
        self.processes = processes
        self.n = len(processes)
        self.total_waiting_time = 0
        self.total_turnaround_time = 0
        self.current_time = 0
        self.completed_processes = []

    def run(self):
        while len(self.completed_processes) < self.n:
            shortest_process = None
            for process in self.processes:
                if process['arrival_time'] <= self.current_time and process not in self.completed_processes:
                    if shortest_process is None or process['burst_time'] <= shortest_process['burst_time']:
                        shortest_process = process
            if shortest_process is None:
                self.current_time = self.processes[0]['arrival_time']
            else:
                shortest_process['waiting_time'] = self.current_time - shortest_process['arrival_time']
                shortest_process['turnaround_time'] = shortest_process['waiting_time'] + shortest_process['burst_time']
                self.total_waiting_time += shortest_process['waiting_time']
                self.total_turnaround_time += shortest_process['turnaround_time']
                self.completed_processes.append(shortest_process)
                self.current_time += shortest_process['burst_time']

        avg_waiting_time = self.total_waiting_time / self.n
        avg_turnaround_time = self.total_turnaround_time / self.n

        # Print the results
        print("Process\t\tBurst Time\tWaiting Time\tTurnaround Time")
        for process in self.completed_processes:
            print("{}\t\t{}\t\t{}\t\t{}".format(process['id'], process['burst_time'],
              process['waiting_time'], process['turnaround_time']))
        print("Average waiting time:", avg_waiting_time)
        print("Average turnaround time:", avg_turnaround_time)




