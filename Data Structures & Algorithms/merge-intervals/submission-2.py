class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_lists = sorted(intervals, key=lambda x: x[0])
        
        i = 1
        ans=[]
        temp = []
        temp.append(sorted_lists[0][0])
        temp.append(sorted_lists[0][1])
        
        while i < len(sorted_lists):
            if sorted_lists[i][0] <= temp[1]:
                temp[1] = max(sorted_lists[i][1], temp[1])       
            else:
                ans.append(list(temp))
                temp[0] = sorted_lists[i][0]
                temp[1] = sorted_lists[i][1]
            i=  i+1
            
        ans.append(temp)
        return ans