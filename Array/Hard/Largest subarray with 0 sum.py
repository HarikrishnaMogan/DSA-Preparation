https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1?category%5B%5D=Hash&company%5B%5D=Amazon&page=1&query=category%5B%5DHashcompany%5B%5DAmazonpage1company%5B%5DAmazoncategory%5B%5DHash&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-subarray-with-0-sum

sum = 0
        map = dict()
        maxi = 0
        for i in range(n):
            sum+=arr[i]
            if sum == 0:
                maxi = max(maxi,i+1)
            
            rem = sum -0
            if rem in map:
                l = map[rem]
                maxi = max(maxi, i-l)
            if sum not in map:
                map[sum] = i
        return maxi
            
