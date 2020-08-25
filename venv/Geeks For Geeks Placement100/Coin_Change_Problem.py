#Coin Change Problem Problem [GFG Placement 100 Q2]
#Problem statement - An array of coins is given and a sum value
#to count total no of ways to get sum by using coins
#coins supply - infinite

#Recursion logic
#if n i.e length of list becomes 0 we return 0
#if sum becomes 0 than we can choose any coin so returning 1
#if the coin value is greater than sum value we recur for n-1 list length
#and thus we are not including it in our count
#else if the coin value is less than or equal to sum value
#we decrease the sum value with coin value and increasing the count
#also as there is infinite supply of coins so we dont decrease the n value
#new sum becoing sum-coin value and now we recur upon these parameters
#this problem has overlapping subproblems
#to optimise soln memoized code named memoCountWays is there
#Note-taking sum as col and n as row will not work

#Recursive Approach
def countWays(l,n,sum):
    if n==0:
        return 0
    if sum==0:
        return 1
    res=countWays(l,n-1,sum)
    if l[n-1]<=sum:
        res+=countWays(l,n,sum-l[n-1])
    return res

#Top Down / Tabulation / Memoized Approach
def memoCountWays(l,n,sum):
    memo=[[-1]*(sum+1)]*(n+1)
    if memo[n][sum]!=-1:
        return memo[n][sum]
    if n==0:
        return 0
    if sum==0:
        return 1
    memo[n][sum]=memoCountWays(l,n-1,sum)
    if l[n-1]<=sum:
        memo[n][sum]+=memoCountWays(l,n,sum-l[n-1])
    return memo[n][sum]

#Bottom up / Dynamic Programming Approach
def dpCountWays(S, m, n):
    table = [[0 for x in range(m)] for x in range(n + 1)]
    for i in range(m):
        table[0][i] = 1
    for i in range(1, n + 1):
        for j in range(m):
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0
            y = table[i][j - 1] if j >= 1 else 0
            table[i][j] = x + y
    return table[-1][-1]

if __name__=='__main__':
    l=list(map(int,input().split()))
    sum=int(input())
    #print(countWays(l,len(l),sum))
    #print(memoCountWays(l,len(l),sum))
    #print(dpCountWays(l,len(l),sum))