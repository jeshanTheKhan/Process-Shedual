def main():
    n=int(input("Enter The Process Number : "))
    bt=[]
    wt=[0]*n 
    awt=0


    for a in range(n):
        brust_time=int(input(f"Process {a+1} Brust Time : "))
        bt.append(brust_time)

    for i in range(1,n):
        wt[i]=wt[i-1]+bt[i-1]
        awt+=wt[i]


    awt/=n 

    print(f"Average Wating Time : {awt:.2f}")

if __name__ =="__main__":
    main()