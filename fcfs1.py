def buble_sort(n,at,bt,pid):
    
    for i in range(n-1):
        for j in range(n-i-1):
            if at[j]>at[j+1]:
                at[j],at[j+1]=at[j+1],at[j]
            
                bt[j],bt[j+1]=bt[j+1],bt[j]
            
                pid[j],pid[j+1]=pid[j+1],pid[j]


def main():
    n=int(input("Enter The Process Number : "))
    bt=[]
    at=[]
    wt=[0]*n
    pid=[]
    awt=0
    
    for a in range(n):
        pid.append(a+1)
        print(f"Process {a+1} : ")
        arrival_time=int(input(f"Process {a+1} Arrival time : "))
        brust_time=int(input(f"Process {a+1} brust time : "))
        at.append(arrival_time)
        bt.append(brust_time)
    buble_sort(n,at,bt,pid)
        
        
    wt[0]=0
    total_time=at[0]+bt[0]
        
    for i in range(1,n):
        total_time=max(total_time,at[i])
        wt[i]=total_time-at[i]
        total_time+=bt[i]
        awt+=wt[i]
        
        awt/=n
        
    print("\nProcess\tArrival Time\tBrust Time\tWating Time")
    for i in range(n):
         print(f"{pid[i]}\t\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}")   
    
    
    print(f"Average Waiting Time : {awt:.2f}")


if __name__ == "__main__":
    main()