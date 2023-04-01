import matplotlib.pyplot as plt

class sjfNonPreemptive:
    def __init__(self, processes):
        self.processes = processes
        self.n = len(processes)
        self.total_waiting_time = 0
        self.total_turnaround_time = 0
        self.current_time = 0
        self.completed_processes = []
        self.gantt_chart = []

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
                self.gantt_chart.append((shortest_process['id'], self.current_time, self.current_time + shortest_process['burst_time'], shortest_process['burst_time']))
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

        # Draw the gantt chart
        fig, gnt = plt.subplots()
        gnt.set_ylim(0, 10)
        gnt.set_xlim(0, self.current_time + 5)
        gnt.set_xlabel('Time')
        gnt.set_ylabel('Process')
        gnt.set_yticks([i+0.5 for i in range(self.n)])
        gnt.set_yticklabels(['P{}'.format(i+1) for i in range(self.n)])
        gnt.grid(True)

        for i in range(len(self.gantt_chart)):
            process_id, start_time, end_time, burst_time = self.gantt_chart[i]
            color = 'C{}'.format(process_id % 10)
            gnt.broken_barh([(start_time, burst_time)], (i, 0.6), facecolors=color, edgecolors='black')
            gnt.annotate('P{}'.format(process_id), (start_time+burst_time/2, i+0.3), ha='center', va='center', color='white', fontweight='bold')

        plt.show()

