def knapsack(maxw,val,wt,n,memo):
    
    if n == 0 or maxw == 0 :
        # memo[n][maxw] = 0
        return 0
    if memo[n][maxw] != 0:
        return memo[n][maxw]
    if wt[n-1]<=maxw:
        memo[n][maxw] = (max(val[n-1]+knapsack(maxw-wt[n-1],val,wt,n-1,memo),knapsack(maxw,val,wt,n-1,memo)))
        # print(memo)
        return memo[n][maxw]
    else:
        memo[n][maxw] = knapsack(maxw,val,wt,n-1,memo)
        return memo[n][maxw]
    
if __name__ == "__main__":
    #maxw=5
    #val=[12,10,20,15]
   # wt=[2,1,3,2]
    maxw = int((input("Enter Weight of Sack : ")))
    val = list(map(int, input("Enter Profit : ").split()))
    wt = list(map(int, input("Enter weights : ").split()))

    memo = [[0 for i in range(maxw + 1)] for j in range(len(val) + 1)]
    print("Maximun Profit :",knapsack(maxw,val,wt,len(val),memo))
    print("Memoization : ")
    for i in memo:
        print(i)
