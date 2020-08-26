#Edit Distance Problem [GFG Placement 100 Q3]
#Problem statement - two strings s1 and s2,we can do three
#operations insert,delete and replace to make string s1 to s2
#return the min no of steps required for conversion
#we can so either insert,delete or replace one operation at a time

#Recursion logic
#we start from the last of both strings s1 and s2
#length are m and n respectively, if char at ith index of
#string s1 is equal to char at ith of string s2
#we check for m-1 and n-1 part of string
#talking about base condition if any of the string either
#s1 or s2 become empty so the only possible least operation to
#convert empty to non empty string is either do len(non empty str) deletion
#in non empty or to insert total elements in empty string
#thus min operations==len(non empty str)
#Recursion logic
#ex- s1=SATURDAY s2=SUNDAY till m-2 and n-2 index char are same
# at SATUR and SUN R!=N so if we delete SATU and SUN
#if we insert SATURN and SUN SO SATU and SUN
#if we replace SATUN and SUN so SATU and SU
#we will choose the min of these three and recur over left over string again

#Recursive Approach
def recurEdit(s1,s2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1]==s2[n-1]:
        return recurEdit(s1,s2,m-1,n-1)
    return 1+min(recurEdit(s1,s2,m,n-1),recurEdit(s1,s2,m-1,n),recurEdit(s1,s2,m-1,n-1))

def memoEdit(s1,s2,m,n):
    memo=[[-1]*(n+1)]*(m+1)
    if memo[m][n]!=-1:
        return memo[m][n]
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1]==s2[n-1]:
        memo[m][n]=recurEdit(s1,s2,m-1,n-1)
    memo[m][n]=1+min(recurEdit(s1,s2,m,n-1),recurEdit(s1,s2,m-1,n),recurEdit(s1,s2,m-1,n-1))
    return memo[m][n]

def dpEdit(s1,s2,m,n,dp):
    for i in range(m+1):
        dp[i][0]=i
    for j in range(n+1):
        dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[-1][-1]

if __name__=='__main__':
    s1=input()
    s2=input()
    m,n=len(s1),len(s2)
    dp = [[-1] * (n + 1)] * (m + 1)
    #print(recurEdit(s1,s2,m,n))
    #print(memoEdit(s1, s2, m, n))
    #print(dpEdit(s1, s2, m, n, dp))
