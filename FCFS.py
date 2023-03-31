class FCFS:
    # Get input from user
    def get_input(self, noProcess):
        list = []
        noProcess = int(input("Enter Number of process: "))
        for i in range(noProcess):
            temp = []
            name_of_process = input("Enter Name of process: ")
            arrival_time = int(input(f"Enter Arrival Time of {name_of_process}: "))

            burst_time = int(input(f"Enter Burst Time of {name_of_process}: "))

            temp.extend([name_of_process, arrival_time, burst_time])
            list.append(temp)
        FCFS.schedulingProcess(self, list)
    
    def schedulingProcess(self, list):
        list.sort(key=lambda x: x[1])
        start_time = []
        exit_time = []
        s_time = 0
        for i in range(len(list)):
            if s_time < list[i][1]:
                s_time = list[i][1]
            start_time.append(s_time)
            s_time = s_time + list[i][2]
            e_time = s_time
            exit_time.append(e_time)
            list[i].append(e_time)
        t_time = FCFS.calculateTurnaroundTime(self, list)
        w_time = FCFS.calculateWaitingTime(self, list)
        FCFS.printData(self, list, t_time, w_time)
    
    def calculateTurnaroundTime(self, list):
        total_turnaround_time = 0
        for i in range(len(list)):
            turnaround_time = list[i][3] - list[i][1]
            
            # turnaround_time = completion_time - arrival_time
            
            total_turnaround_time = total_turnaround_time + turnaround_time
            list[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(list)
        
        # average_turnaround_time = total_turnaround_time / no_of_processes
        
        return average_turnaround_time
    
    def calculateWaitingTime(self, list):
        total_waiting_time = 0
        for i in range(len(list)):
            waiting_time = list[i][4] - list[i][2]
            
            #waiting_time = turnaround_time - burst_time
            
            total_waiting_time = total_waiting_time + waiting_time
            list[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(list)
        
        # average_waiting_time = total_waiting_time / no_of_processes
        
        return average_waiting_time

    def printData(self, list, average_turnaround_time, average_waiting_time):

        print("Process_ID\t\tArrival_Time\t\tBurst_Time\t\tCompletion_Time\t\tTurnaround_Time\t\tWaiting_Time")

        for i in range(len(list)):
            for j in range(len(list[i])):
                print(list[i][j], end="\t\t\t")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

    def run(self):
        self.get_input(self)
        
    # def get_calculate(self):    
    #     # inisialisasi waktu waiting dan waktu turnaround dengan nilai nol
    #     current_time = 0
            
    #     # ini buat prosesnya
    #     for i in range(len(self.queue)):
    #     # kalo queuenya masih kosong
    #         if i == 0:
    #             current_time = self.queue[i]['arrival_time']
    #             #self.queue[i]['waiting_time'] = 
    #             #current_time = self.__arrival_time[i]
    #         else:
    #             # proses berikutnya dimulai setelah proses sebelumnya selesai

    #             current_time += self.queue[i-1]['burst_time']

    #             # kemudian hitung waiting time dan turnaround time
    #         self.queue[i]['waiting_time'] = current_time - self.queue[i]['arrival_time']
    #         self.queue[i]['turnaround_time'] = self.queue[i]['waiting_time'] + self.queue[i]['burst_time']
    #         # hitung nilai rata-rata waiting time dan turnaround time
    #         avg_waiting_time = sum(self.queue[i]['waiting_time'])
    #         avg_turnaround_time = sum(self.queue[i]['turnaround_time'])  

    #     print("Processes\t Burst Time\t Waiting Time\t Turnaround Time")
    #     for i in range(len(self.queue)):
    #         print(self.queue[i]['name'], "\t\t", self.queue[i]['burst_time'], "\t\t", self.queue[i]['waiting_time'], "\t\t", self.queue[i]['turnaround_time'])

    #     print("\nAverage waiting time = {:.2f}".format(avg_waiting_time))
    #     print("Average turnaround time = {:.2f}".format(avg_turnaround_time))

    # def run(self):
    #     self.get_input()
    #     self.get_calculate()





# def fifo(processes, n, burst_time):
#     # inisialisasi waktu waiting dan waktu turnaround dengan nilai nol
#     waiting_time = [0] * n
#     turnaround_time = [0] * n
    
#     # inisialisasi queue atau antrian dan waktu sekarang
#     queue = []
#     current_time = 0
    
#     # ini buat prosesnya
#     for i in range(n):
#         # kalo queuenya masih kosong
#         if not queue:
#             current_time = processes[i]
#         else:
#             # proses berikutnya dimulai setelah proses sebelumnya selesai
#             current_time += burst_time[i-1]
        
#         # tambahin prosesnya ke queue
#         queue.append(processes[i])
        
#         # kemudian hitung waiting time dan turnaround time
#         waiting_time[i] = current_time - processes[i]
#         turnaround_time[i] = waiting_time[i] + burst_time[i]
    
#     # tampilkan hasil penghitungan untuk setiap prosesnya
#     print("Processes\t Burst Time\t Waiting Time\t Turnaround Time")
#     for i in range(n):
#         print(processes[i], "\t\t", burst_time[i], "\t\t", waiting_time[i], "\t\t", turnaround_time[i])
    
#     # hitung nilai rata-rata waiting time dan turnaround time
#     avg_waiting_time = sum(waiting_time)
#     avg_turnaround_time = sum(turnaround_time)
    
#     print("\nAverage waiting time = {:.2f}".format(avg_waiting_time))
#     print("Average turnaround time = {:.2f}".format(avg_turnaround_time))

# # penggunaan fungsi buat proses fifonya
# if __name__ == "__main__":
#     processes = [1, 2, 3, 4, 5] # daftar proses
#     n = len(processes) # jumlah proses
#     burst_time = [5, 2, 8, 1, 4] # burst time untuk setiap proses

#     fifo(processes, n, burst_time)