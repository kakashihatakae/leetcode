class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_sum = 0
        
        for t in range(len(triangle)-2,-1, -1):
            for s in range(len(triangle[t])):
                temp= min(triangle[t+1][s],triangle[t+1][s+1])
                triangle[t][s] += temp
        return triangle[0][0]
                
            
