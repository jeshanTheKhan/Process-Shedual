def main():
    n=int(input("Enter The Process Number : "))
    bt=[]
    wt=[0]*n
    pr=[]
    awt=0

    for a in range(n):
        brust_time=int(input(f"Process {a+1} brust time : "))
        priority=int(input(f"Process {a+1} priority : "))
        bt.append(brust_time)
        pr.append(priority)

    for i in range(n):
        pos=i
        for j in range(i+1,n):
            if pr[pos] > pr[j]:
                pos=j

        pr[i],pr[pos] = pr[pos],pr[i]

        bt[i],bt[pos] = bt[pos],bt[i]

    
    for i in range(1, n):
        wt[i] = wt[i - 1] + bt[i - 1]
        awt += wt[i]

    awt/=n

    print(f"Average Wating Time : {awt:.2f}")


if __name__ == "__main__":
    main()