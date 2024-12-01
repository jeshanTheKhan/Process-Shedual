def main():
    n = int(input("Enter The Number Of Process: "))
    tq = int(input("Enter The Time Quantum: "))

    cnt = 0
    time_e = 0
    wt = [0] * n 
    bt = []  
    rem_bt = []  
    tat = [0] * n  
    total_tat = 0
    total_wt = 0


    for a in range(n):
        burst_time = int(input(f"Process {a + 1} Burst Time: "))
        bt.append(burst_time)
        rem_bt.append(burst_time)


    while cnt < n:
        for i in range(n):
            if rem_bt[i] > 0:  # Process is not yet completed
                time_spend = min(rem_bt[i], tq)
                rem_bt[i] -= time_spend
                time_e += time_spend

                if rem_bt[i] == 0:  # Process has completed
                    cnt += 1
                    tat[i] = time_e  # Turnaround time
                    wt[i] = tat[i] - bt[i]  # Waiting time
                    total_wt += wt[i]
                    total_tat += tat[i]


    avg_wt = total_wt / n
    avg_tat = total_tat / n

    # Print results
    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{i + 1}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


if __name__ == "__main__":
    main()
