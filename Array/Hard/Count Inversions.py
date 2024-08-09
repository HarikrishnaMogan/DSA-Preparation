https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=inversion-of-array

def merge(arr, l, h):
            mid = (l+h)//2
            left = l
            right = mid+1
            temp = []
            count = 0
            while left <=mid and right <=h:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    count = mid-left+1
                    temp.append(arr[right])
                    right+=1
            while left <=mid:
                temp.append(arr[left])
                left+=1
            while right <=h:
                temp.append(arr[right])
                right+=1
            
            for i in range(l,h+1):
                arr[i] = temp[i-l]
            return count
