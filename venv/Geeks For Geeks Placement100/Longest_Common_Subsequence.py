#Longest Common Subsequence Problem [GFG Placement 100 Q1]
#Problem statement - two strings s1 and s2,find out the length
#                    of the longest common subsequence

#Recursion logic
#we start from the last of both strings s1 and s2
#length are m and n respectively, if char at ith index of
#string s1 is equal to char at ith of string s2
#+1 and return else we delete last char from s1 and recur for
#rest of the string length i.e m-1 as well as we delete last char from
#s2 and recur for n-1 length
#talking about base condition if either m or n becomes 0
#we return 0 to the parent
#this problem has overlapping subproblems
#to optimise soln memoized code named lcsMemo is there

#Recursive Approach
def lcs(s1,s2,m,n):
    if not m or not n:
        return 0
    elif s1[m-1]==s2[n-1]:
        return 1+lcs(s1,s2,m-1,n-1)
    else:
        return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))

#Top Down / Tabulation / Memoized Approach
def lcsMemo(s1,s2,m,n):
    memo=[[-1]*(n+1)]*(m+1)
    if memo[m][n]!=-1:
        return memo[m][n]
    if not m or not n:
        memo[m][n]=0
    elif s1[m-1]==s2[n-1]:
        memo[m][n]=1+lcs(s1,s2,m-1,n-1)
    else:
        memo[m][n]=max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
    return memo[m][n]

#Bottom up / Dynamic Programming Approach
def lcsDP(s1,s2,m,n):
    dp=[[0]*(n+1)]*(m+1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

if __name__=='__main__':
    s1 = input()
    s2 = input()
    m,n=len(s1),len(s2)
    #print(lcs(s1,s2,m,n))
    #print(lcsMemo(s1,s2,m,n))
    print(lcsDP(s1,s2,m,n))