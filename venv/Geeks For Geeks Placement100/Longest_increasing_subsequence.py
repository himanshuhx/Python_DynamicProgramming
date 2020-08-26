#longest Increasing Subsequence [GFG Placement 100 Q4]
#problem statement - an array is given we have to find the length of
#the longrst increasing subsequence
#This recursive approach has O(M*N) time complexity
#For more optimization we can use binary search which has time complexity of O(nlogn).

#Recursive Approaach
#we are maintaining a lis[n] which uses extra auxillary space.O(n)
#[10, 5, 18, 7, 2, 9] let it be the input arr.
#we initialize lis[0]=1 as in worse case if array is sorted as sorted(arr,reverse=True)
#i.e descending order, thus having no increasing subsequence.In this case answer will be 1
#as each element is itself a increasing subsequence
#lis=[1,0,0,0,0,0] we check for 5 is there any ele to the left of 5 which is less than 5
#if yes check for current value of lis[i] and lis[j]+1 +1 because we found another ele of subsequence
#append it to lis continue till last ele
# return max ele of lis[] our required answer

#DP Approach
def lis(arr,n):
    lis=[0]*n
    lis[0]=1
    for i in range(n):
        lis[i]=1
        for j in range(1,i):
            if arr[i]<arr[j]:
                 lis[i]=max(lis[i],lis[j]+1)
    return max(lis)

#Optimized Approach Using Binary Search
def lisBinary(arr,n):
    lis=[arr[0]]
    len=1
    for i in range(n):
        if arr[i]>lis[len-1]:
            lis.append(arr[i])
            len+=1
        else:
            idx=binarySearch(lis,0,len-1,arr[i])
            lis[idx]=arr[i]
    return len

def binarySearch(lis,start,end,ele):
    while start<end:
        idx = start + (end-start)//2
        if lis[idx]>=ele:
            end=idx
        else:
            start=idx+1
    return start

l=list(map(int,input().split()))
#print(lis(l,len(l)))
#print(lisBinary(l,len(l)))