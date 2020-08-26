#Minimum count of coins to make a value [GFG Placement 100 Q6]
#problem statement - an array of coins is given we have to find the minimum
#no of coins to make a required value

#Recursive Approach

def recurCoins(coins,n,val):
    res=float('inf')
    if val==0:
        return 0
    for i in range(n):
        if coins[i]<=val:
            ans=recurCoins(coins,n,val-coins[i])
            if ans!=float('inf'):
                res=min(res,ans+1)
    return res

#Tabulation Approach
#Time complexity theta(n*val)
#Auxillary space theta(val)

def dpCoins(coins,n,val):
    dp=[float('inf')]*(val+1)
    dp[0]=0
    for i in range(1,val+1):
        for j in range(n):
            if i>=coins[j]:
                ans=dp[i-coins[j]]
                dp[i]=min(dp[i],ans+1)
    return dp[-1]

coins=list(map(int,input().split()))
val=int(input())
#print(recurCoins(coins,len(coins),val))
#print(dpCoins(coins,len(coins),val))