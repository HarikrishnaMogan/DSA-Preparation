
https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/
#Better approch

def longConsSeq(arr):
    if len(arr) == 0:
        return 0
    arr.sort()
    long = 1
    lastSamllElement = arr[0]
    count = 1
    i = 1
    while i < len(arr):
        if arr[i]-1 == lastSamllElement:
            count+=1
            lastSamllElement = arr[i]
        elif arr[i] != lastSamllElement:
            count = 1
            lastSamllElement = arr[i]
        long = max(long,count)
        i+=1
    return long

print(longConsSeq([100, 200, 1, 3, 2, 4, 1,1,2,2,101]))
