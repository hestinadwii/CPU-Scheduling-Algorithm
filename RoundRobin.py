import matplotlib.pyplot as plt

class RoundRobin:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = i+1
            arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            process_data.append(temporary)
        
        time_slice = int(input("Enter Time Slice: "))

        RoundRobin.schedulingProcess(self, process_data, time_slice, no_of_processes)
    
    def schedulingProcess(self, process_data, time_slice, no_of_processes):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        current_time = 0
        process_data.sort(key=lambda x: x[1])
        
        while 1:
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= current_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i]
                                    [1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert(
                                    (len(ready_queue) - 1), ready_queue.pop(k))
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i]
                                [1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > time_slice:
                    start_time.append(current_time)
                    current_time = current_time + time_slice
                    end_time = current_time
                    exit_time.append(end_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= time_slice:
                    start_time.append(current_time)
                    current_time = current_time + ready_queue[0][2]
                    end_time = current_time
                    exit_time.append(end_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(end_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if current_time < normal_queue[0][1]:
                    current_time = normal_queue[0][1]
                if normal_queue[0][2] > time_slice:
                    start_time.append(current_time)
                    current_time = current_time + time_slice
                    end_time = current_time
                    exit_time.append(end_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                elif normal_queue[0][2] <= time_slice:
                    start_time.append(current_time)
                    current_time = current_time + normal_queue[0][2]
                    end_time = current_time
                    exit_time.append(end_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(end_time)
        t_time = RoundRobin.calculateTurnaroundTime(self, process_data)
        w_time = RoundRobin.calculateWaitingTime(self, process_data)
        RoundRobin.printData(self, process_data, t_time,
                             w_time, executed_process)
        
        # create Gantt chart
        fig, gnt = plt.subplots()
        gnt.set_title("Gantt Chart - Round Robin")
        gnt.set_xlabel('Time')
        gnt.set_ylabel('Processes')
        gnt.set_ylim(0, no_of_processes + 1)
        gnt.set_xlim(0, process_data[-1][5] + 5)
        gnt.set_yticks(range(1, no_of_processes + 1))
        gnt.set_yticklabels([f'P{i}' for i in range(1, no_of_processes + 1)])

        for i in range(len(start_time)):
            gnt.broken_barh([(start_time[i], exit_time[i] - start_time[i])],
                            (executed_process[i]-1, 1), facecolors=('tab:blue'))

        plt.show()

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            # turnaround_time = completion_time - arrival_time
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        # average_turnaround_time = total_turnaround_time / no_of_processes
        average_turnaround_time = total_turnaround_time / len(process_data)
        
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            # waiting_time = turnaround_time - burst_time
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        # average_waiting_time = total_waiting_time / no_of_processes
        average_waiting_time = total_waiting_time / len(process_data)
        
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, executed_process):
        print("\n ___________________________________________________________________________________________________________________________________") 
        print("|                                                                                                                                   |") 
        print("|						        Round Robin Scheduling  					            |") 
        print("|___________________________________________________________________________________________________________________________________|") 
        print("\nProcess_ID\t\tArrival_Time\t\tBurst_Time\t\tCompletion_Time\t\tTurnaround_Time\t\tWaiting_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                if j not in (2, 3):
                    print(process_data[i][j], end="\t\t\t")
            print()

        print()
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'Sequence of Processes: {executed_process}')
        
    def run(self):
        no_of_processes = int(input("Enter number of processes: "))
        self.processData(no_of_processes)