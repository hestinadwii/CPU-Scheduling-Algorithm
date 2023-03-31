from FCFS import FCFS
#from sjfNonPreemptive import sjfNonPreemptive
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
    # elif option == 2:
    #     sjfNonPreemptive = sjfNonPreemptive(input())

