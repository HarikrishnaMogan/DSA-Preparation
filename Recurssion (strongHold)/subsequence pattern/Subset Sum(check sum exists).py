
https://www.naukri.com/code360/problems/subset-sum_630213?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.
    def subseq(i,k,a,n,total):
        if i == n:
            if k == total:
                return True
            return False
        
        total += a[i]
        if subseq(i+1,k,a,n,total)==True:
            return True
        
        total-=a[i]
        if subseq(i+1,k,a,n,total)==True:
            return True
        
        return False
    return subseq(0,k,a,n,0)
