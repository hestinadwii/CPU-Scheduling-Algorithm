import matplotlib.pyplot as plt

class ShortestJobFirst:
    def __init__(self, processes):
        self.processes = processes
        self.p = len(processes)
        self.total_time = 0
        self.process_left = len(processes)
        self.current_time = 0
        self.current_process = -1
        self.gantt_chart = []

    def shortest_job_first(self):
        while self.process_left > 0:
            # Check which processes have arrived
            available_processes = []
            for i in range(self.p):
                if self.processes[i][1] <= self.current_time and self.processes[i][3] == 0: # process hasn't completed yet
                    available_processes.append(i)

            if len(available_processes) == 0:
                self.current_time += 1
                continue

            # Find process with smallest burst time
            shortest_process = available_processes[0]
            for i in range(len(available_processes)):
                if self.processes[available_processes[i]][2] < self.processes[shortest_process][2]:
                    shortest_process = available_processes[i]

            # Add label to gantt chart if a new process is being executed
            if self.current_process != shortest_process:
                if len(self.gantt_chart) > 0:
                    self.gantt_chart[-1].append(self.current_time) # add end time to previous process
                self.gantt_chart.append([self.processes[shortest_process][0], self.current_time]) # add new process
                self.current_process = shortest_process

            # Decrease remaining time of current process
            self.processes[shortest_process][2] -= 1
            remaining_time = self.processes[shortest_process][2]

            # Check if process has completed
            # Check if process has completed
            if remaining_time == 0:
                self.processes[shortest_process][3] = self.current_time + 1 # completion time
                self.processes[shortest_process][4] = self.processes[shortest_process][3] - self.processes[shortest_process][1] - self.processes[shortest_process][2] # waiting time
                self.processes[shortest_process][5] = self.processes[shortest_process][3] - self.processes[shortest_process][1] # turnaround time
                self.process_left -= 1 # update process_left


            # Move time forward
            self.current_time += 1

        # add end time to last process
        if len(self.gantt_chart) > 0:
            self.gantt_chart[-1].append(self.current_time)
            
        print("\nTabel waktu proses")
        print("Proses\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time\tCompletion Time")
        total_waiting_time = 0
        total_turnaround_time = 0
        for i in range(self.p):
            completion_time = self.processes[i][3]
            arrival_time = self.processes[i][1]
            burst_time = self.processes[i][6]
            turnaround_time = completion_time - arrival_time
            waiting_time = turnaround_time - burst_time
            total_waiting_time += waiting_time
            total_turnaround_time += turnaround_time
            print(f"{self.processes[i][0]}\t{self.processes[i][6]}\t\t{self.processes[i][1]}\t\t{waiting_time}\t\t{turnaround_time}\t\t{completion_time}")
        average_waiting_time = total_waiting_time / self.p
        average_turnaround_time = total_turnaround_time / self.p
        print(f"\nWaktu tunggu rata-rata: {average_waiting_time}")
        print(f"Turnaround time rata-rata: {average_turnaround_time}")
        
    def display_gantt_chart(self):
        fig, gantt = plt.subplots()
        gantt.set_xlabel('Time')
        gantt.set_ylabel('Processes')
        for i in range(len(self.gantt_chart)):
            start_time = self.gantt_chart[i][1]
            end_time = self.gantt_chart[i][2]
            colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
            gantt.broken_barh([(start_time, end_time-start_time)], (i, 0.5), facecolors=(colors[i % len(colors)]))
            gantt.text((start_time+end_time)/2, i+0.25, self.gantt_chart[i][0], ha='center', va='center')
        gantt.set_ylim(0, len(self.gantt_chart))
        plt.show()
           

