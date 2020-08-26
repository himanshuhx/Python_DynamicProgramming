#Minimum jumps to reach end Problem [GFG Placement 100 Q7]
#3 4 2 1 2 1 for this arr at i=0 arr[0]=3 aka we can jump upto
#max 3 upcoming index here we can go to 4 2 1
#we have to find the minimum steps to reach the end
#Note - Jump will only be successful if i+arr[i]>=last index of arr.

#Recursive approach
def recurToReach(arr,n):
    ans=float('inf')
    if n==1:
        return 0
    for i in range(n-1):
        if i+arr[i]>=n-1:
            sub_res=recurToReach(arr,i+1)
            ans=min(ans,sub_res+1)
    return ans

#DP Approach
#Time complexity O(n^2)
#Auxillary space O(n+1)
def dpToReach(arr,n):
    dp=[float('inf')]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        for j in range(i):
            if j+arr[j]>=i:
                dp[i]=min(dp[i],dp[j]+1)
    return dp[-1]

arr=list(map(int,input().split()))
#print(recurToReach(arr,len(arr)))
#print(dpToReach(arr,len(arr)))