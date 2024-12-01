def sort(at, bt, n, pid):
    for i in range(n):
        for j in range(n - i - 1):
            if at[j] > at[j + 1] or (at[j] == at[j + 1] and bt[j] > bt[j + 1]):
                at[j], at[j + 1] = at[j + 1], at[j]
                bt[j], bt[j + 1] = bt[j + 1], bt[j]
                pid[j], pid[j + 1] = pid[j + 1], pid[j]


def main():
    n = int(input("Enter The Process Number: "))
    at = []
    bt = []
    wt = [0] * n
    pid = []  
    awt = 0

    # Input processes data
    for a in range(n):
        arrival_time = int(input(f"Process {a + 1} Arrival Time: "))
        burst_time = int(input(f"Process {a + 1} Burst Time: "))

        at.append(arrival_time)
        bt.append(burst_time)
        pid.append(a + 1)  # Process ID


    sort(at, bt, n, pid)


    current_time = at[0] 
    for i in range(n):
        if current_time < at[i]: 
            current_time = at[i]
        wt[i] = current_time - at[i]
        current_time += bt[i]  
        awt += wt[i]


    awt /= n


    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time")
    for i in range(n):
        print(f"{pid[i]}\t\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}")

    print(f"\nAverage Waiting Time: {awt:.2f}")


if __name__ == "__main__":
    main()
