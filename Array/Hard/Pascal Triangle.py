#Find element at pascal triangle, where Row = 5, column = 3
#easiest way to solve is using formula, (row-1)C(column-1) eg:nCr formula => n!/r!*(n-r)!
#7C3 => 7!/3!*5! => (7*6*5*4*3*2*1)/(3*2*1)*(5*4*3*2*1) => 7*6*5/3*2*1 - if you observe 7 multiplied by # places and divided by 3! gives the same answer

def getElementOfPascal(row,column):
    n = row-1
    r = column-1
    ans = 1
    for i in range(r):
        ans = ans *(n-i)
        ans =  ans/(i+1)
    return int(ans)

# print(getElementOfPascal(5,3))  

#print Nth row of a pascal triangle

def generateRow(n):
    ans = 1
    temp = [1]
    for i in range(1,n):
        ans = ans*(n-i)
        ans = ans//i
        temp.append(ans)
    return temp

#print(generateRow(5))

#print the pascal triangle, strivers solution
def printPasacl(n):
    ans = []
    for i in range(n):
        ans.append(generateRow(i+1))
    return ans

print(printPasacl(5))
................................................................................
https://leetcode.com/problems/pascals-triangle/
#my solution

        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(2, numRows):
            k = ans[i-1]
            for j in range(len(k)):
                if j==0:
                    ans.append([1])
                else:
                    sum = ans[i-1][j-1]+ans[i-1][j]
                    ans[i].append(sum)
            ans[i].append(1)
        return ans
