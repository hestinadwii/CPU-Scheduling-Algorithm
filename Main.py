from FCFS import FCFS
from sjfNonPreemptive import sjfNonPreemptive
from sjfPreemptive import ShortestJobFirst
from PriorityPreemptive import P_Priority
from PriorityNonPreemtive import NP_Priority


fcfs = FCFS()

while True:
    print("1. FCFS")
    print("2. SJF Non-Preemptive")
    print("3. SJF Preemptive")
    print("4. Round Robin")
    print("5. Priority Non-Preemptive")
    print("6. Priority Preemptive")
    print("0. Exit from Program")
    option = int(input("\nEnter the Number's Menu: "))

    if option == 1:
        fcfs.run()
    elif option == 2:
        if __name__ == "__main__":
            n = int(input("Enter number of processes: "))
            processes = []
            for i in range(n):
                arrival_time = int(
                    input("Enter arrival time of process {}: ".format(i+1)))
                burst_time = int(
                    input("Enter burst time of process {}: ".format(i+1)))
                process = {'id': i+1, 'arrival_time': arrival_time,
                           'burst_time': burst_time, 'waiting_time': None, 'turnaround_time': None}
                processes.append(process)

            sjf = sjfNonPreemptive(processes)
            sjf.run()
    elif option == 3:
        if __name__ == "__main__":
            p = int(input("Enter number of processes: "))
            processes = []
            for i in range(p):
                process_id = input(f"Masukkan ID proses {i+1}: ")
                arrival_time = int(input(f"Masukkan waktu kedatangan proses {i+1}: "))
                burst_time = int(input(f"Masukkan waktu burst proses {i+1}: "))
                processes.append([process_id, arrival_time, burst_time, 0, 0, 0, burst_time])

            sjf = ShortestJobFirst(processes)
            sjf.shortest_job_first()
            sjf.display_gantt_chart()
    
    elif option == 5:
        if __name__ == "__main__":
            no_of_processes = int(input("Enter number of processes: "))
            priority = NP_Priority()
            priority.processData(no_of_processes)
            
    elif option == 6:
        if __name__ == "__main__":
            no_of_processes = int(input("Enter number of processes: "))
            priority = P_Priority()
            priority.processData(no_of_processes)


