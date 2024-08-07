https://www.interviewbit.com/problems/subarray-with-given-xor/
# xor =  x ^ b
# xor ^ b = x ^ b^ b
# xor ^ b = x
# x = xor ^ b

map = dict()
        map[0] = 1 
        xor = 0
        count = 0
        for i in A:
            xor = xor ^ i
            x = xor ^ B
            if x in map:
                count += map[x]
            if xor in map:
                map[xor] +=1
            else:
                map[xor] =1
        return count
