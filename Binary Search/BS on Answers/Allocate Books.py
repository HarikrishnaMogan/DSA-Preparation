https://www.naukri.com/code360/problems/allocate-books_1090540?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTabValue=PROBLEM

def findPages(arr: [int], n: int, m: int) -> int:

    # Write your code here
    # Return the minimum number of pages
    def countStudent(arr,maxPages,m):
        pages=0
        st=1
        for i in range(len(arr)):
            if pages+arr[i] <= maxPages:
                pages+=arr[i]
            else:
                st+=1
                pages=arr[i]
        return st

    if len(arr) < m:
        return -1

    low = max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        noOfst = countStudent(arr,mid,m)
        if noOfst == m:
            high=mid-1
        elif noOfst >m:
            low = mid+1
        else:
            high = mid-1
    return low

