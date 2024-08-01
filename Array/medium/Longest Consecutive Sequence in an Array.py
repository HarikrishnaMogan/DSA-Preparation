
https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/
#Better approch
TC - Nlog(N), SC - O(1)

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

................................................................

#optimal approch
TC - O(N), SC- O(N)
def longConsSeq(arr):
    if len(arr) == 0:
        return 0
    arrSet = set() #useds set to filter out unique elements
    for i in arr:
        arrSet.add(i)
    count = 0
    long = 1
    for i in arrSet:
        x = i
        count = 0
        if x-1 not in arrSet: #checked if x-1 is present if not looping through to count the sequence
            while x in arrSet:
                count+=1
                x+=1
            long = max(long, count)
    return long
            


print(longConsSeq([100, 200, 1, 3, 2, 4, 1,1,2,2,101]))


