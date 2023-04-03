import matplotlib.pyplot as plt
from tabulate import tabulate

class P_Priority:

    
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))

            arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))

            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))

            priority = int(input(f"Enter Priority for Process {process_id}: "))

            temporary.extend([process_id, arrival_time, burst_time, priority, 0, burst_time])

            process_data.append(temporary)
        P_Priority.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])

        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3],
                                 process_data[i][5]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4],
                                 process_data[i][5]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3])
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:     
                    process_data[k][4] = 1
                    process_data[k].append(e_time - process_data[k][5])
                    process_data[k].append(e_time)        
            if len(ready_queue) == 0:
                normal_queue.sort(key=lambda x: x[1])
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:      
                    process_data[k][4] = 1
                    print(e_time - process_data[k][5]-1, e_time)
                    process_data[k].append(e_time - process_data[k][5])
                    process_data[k].append(e_time)

        t_time = P_Priority.calculateTurnaroundTime(self, process_data)
        w_time = P_Priority.calculateWaitingTime(self, process_data)
        P_Priority.printData(self, process_data, t_time, w_time, sequence_of_process)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][7] - process_data[i][1]

            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)

        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][8] - process_data[i][5]

            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)

        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        process_data.sort(key=lambda x: x[0])

        data=[]
        for process in process_data:
            temp=[]
            temp.extend([process[0], process[3],
              process[1], process[5], process[9], process[8]])
            data.append(temp)

        col_names=["Process","Priority","Arrival Time","Burst Time","Waiting Time","Turnaround Time"]
        print(tabulate(data, headers=col_names))
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'Sequence of Process: {sequence_of_process}')
        processes = [process_data[i][0] for i in range(len(process_data))]
        start_time = [process_data[i][7]-(process_data[i][5]+process_data[i][9]) for i in range(len(process_data))]
        completion_time = [process_data[i][7] for i in range(len(process_data))]
        burst_time = [process_data[i][5]+process_data[i][9] for i in range(len(process_data))]

        fig, gantt_chart = plt.subplots()
        gantt_chart.set_xlim(0, max(completion_time)+5)
        gantt_chart.set_ylim(0, 10)
        gantt_chart.set_title('Gantt Chart - Priority Scheduling')
        gantt_chart.set_xlabel('Time')
        gantt_chart.set_ylabel('Processes')
        gantt_chart.set_yticks([i+0.5 for i in range(len(processes))])
        gantt_chart.set_xticks(range(max(completion_time)+5))
        gantt_chart.set_yticklabels([f'P{i[0]}' for i in process_data])
        gantt_chart.grid(True)
        
        for i in range(len(process_data)):
            color = 'C{}'.format(processes[i] % 10)
            gantt_chart.broken_barh([(start_time[i], burst_time[i])], (i, 0.5), facecolors = color, edgecolors='black')
            gantt_chart.annotate('P{}'.format(processes[i]), (start_time[i]+burst_time[i]/2, i+0.3), ha='center', va='center', color='white', fontweight='bold')
        plt.show()