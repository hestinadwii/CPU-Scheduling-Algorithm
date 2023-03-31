from FCFS import FCFS
from sjfNonPreemptive import sjfNonPreemptive
from sjfPreemptive import Process
from sjfPreemptive import shortest_remaining_time_first
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
                arrival_time = int(input("Enter arrival time of process {}: ".format(i+1)))
                burst_time = int(input("Enter burst time of process {}: ".format(i+1)))
                process = {'id': i+1, 'arrival_time': arrival_time, 'burst_time': burst_time, 'waiting_time': None, 'turnaround_time': None}
                processes.append(process)

            sjf = sjfNonPreemptive(processes)
            sjf.run()
    elif option ==3:
        if __name__ == '__main__':
            num_processes = int(input("Enter number of processes: "))
            processes = []
            for i in range(num_processes):
                pid = f"P{i+1}"
                arrival_time = int(input(f"Enter arrival time for process {pid}: "))
                burst_time = int(input(f"Enter burst time for process {pid}: "))
                processes.append(Process(pid, arrival_time, burst_time))

            completed_processes, avg_waiting_time, avg_turnaround_time = shortest_remaining_time_first(processes)

            print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
            for p in completed_processes:
                print(f"{p.pid}\t\t{p.arrival_time}\t\t{p.burst_time}\t\t{p.waiting_time}\t\t{p.turnaround_time}")

            print(f"\nAverage waiting time: {avg_waiting_time}")
            print(f"Average turnaround time: {avg_turnaround_time}")
