import matplotlib.pyplot as plt

class FCFS:
    def get_input(self, process_data):
        process_data = []
        noProcess = int(input("Enter Number of process: "))
        for i in range(noProcess):
            temp = []
            processID = i+1
            arrival_time = int(input(f"Enter Arrival Time of {processID}: "))

            burst_time = int(input(f"Enter Burst Time of {processID}: "))
            temp.extend([processID, arrival_time, burst_time])
            process_data.append(temp)
        FCFS.calculate(self, process_data)

    def calculate(self, process_data):
        process_data.sort(key=lambda x: x[1])
        start_time = []
        exit_time = []
        current_time = 0
        for i in range(len(process_data)):
            if current_time < process_data[i][1]:
                current_time = process_data[i][1]
            start_time.append(current_time)
            current_time = current_time + process_data[i][2] # burst time
            end_time = current_time
            exit_time.append(end_time)
            process_data[i].append(end_time)
        t_time = FCFS.calculateTurnaroundTime(self, process_data)
        w_time = FCFS.calculateWaitingTime(self, process_data)
        FCFS.printData(self, process_data, t_time, w_time)
        FCFS.gantChart(self, process_data, start_time, exit_time)
    
    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][3] - process_data[i][1]
            
            # turnaround_time = completion_time - arrival_time
            
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        # average_turnaround_time = total_turnaround_time / len(process_data)
        
        return total_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][4] - process_data[i][2]
            
            # waiting_time = turnaround_time - burst_time
            
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        # average_waiting_time = total_waiting_time / len(process_data)
        
        return total_waiting_time

    def printData(self, process_data, turn_around_time, waiting_time):
        print("Process_ID\tArrival_Time\tBurst_Time\tCompletion_Time\tTurnaround_Time\tWaiting_Time")
        for i in range(len(process_data)):
            print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}".format(process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3], process_data[i][4], process_data[i][5]))

        print(f'Average Turnaround Time: {turn_around_time / len(process_data)}')

        print(f'Average Waiting Time: {waiting_time / len(process_data)}')
    
    def gantChart(self, process_data, start_time, exit_time):
        # Plot Gantt chart
        fig, gantt = plt.subplots()
        gantt.set_title('Gantt Chart - FCFS')
        gantt.set_xlabel('Time')
        gantt.set_ylabel('Processes')
        gantt.grid(True)

        gantt.set_yticks([i[0] for i in process_data])
        gantt.set_yticklabels([f'P{i[0]}' for i in process_data])
        # y_ticks = [i[0] for i in process_data]
        # gantt.set_yticks(y_ticks)
        gantt.set_ylim(0, len(process_data) + 1)
        gantt.set_xlim(0, exit_time[-1])
        for i in range(len(process_data)):
            gantt.broken_barh([(start_time[i], process_data[i][2])], (process_data[i][0]-0.4, 0.8), facecolors=('tab:blue'))

        plt.show()
    
    def run(self):
        self.get_input(self)
