https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    def CountPaintersMinTime(arr,maxi,p):
        paintersCount = 1
        board = 0
        for i in range(len(arr)):
            if board+arr[i] <=maxi:
                board+=arr[i]
            else:
                paintersCount+=1
                board=arr[i]
        return paintersCount

    
    if len(boards) < k:
        return -1
    
    low = max(boards)
    high = sum(boards)
    while low <=high:
        mid=(low+high)//2
        paintersCount = CountPaintersMinTime(boards,mid,k)
    
        if paintersCount > k:
            low=mid+1
        else:
            high = mid-1
    return low
