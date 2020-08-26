#Maximum Cuts in Rod Problem Problem [GFG Placement 100 Q5]
#Problem statement - rod length and three different cuts length
#are given. to find maximum cuts possible

#Recursive Approach
def maxCuts(rod,a,b,c):
    if rod<0:
        return -1
    if rod==0:
        return 0
    res=max(maxCuts(rod-a,a,b,c),maxCuts(rod-b,a,b,c),maxCuts(rod-c,a,b,c))
    if res==-1:
        return res
    else:
        return res+1

#Bottom up / Dynamic Programming Approach
def dpMaxCuts(rod,a,b,c):
    dp=[-1]*(rod)
    dp[0]=0
    for i in range(rod):
        if i - a >= 0: dp[i] = max(dp[i], dp[i - a])
        if i - b >= 0: dp[i] = max(dp[i], dp[i - b])
        if i - c >= 0: dp[i] = max(dp[i], dp[i - c])
        if dp[i]!=-1:
            dp[i]+=1
    return dp[-1]



rod,a,b,c=map(int,input().split())
#print(maxCuts(rod,a,b,c))
#print(dpMaxCuts(rod,a,b,c))