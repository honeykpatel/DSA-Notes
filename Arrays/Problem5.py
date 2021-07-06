intervals = [[1,3],[2,6],[8,10],[8,9],[9,11],[15,18],[2,4],[16,17]]

#sort the intervals
intervals.sort()
print(intervals)

#resulting intervals
result = []

#starting with first element
start, end = intervals[0][0], intervals[0][1]

for i in intervals:
    #if interval is not in the current interval
    if i[0]>end:
        #store in result and move forward with new interval
        result.append([start,end])
        #update start and end
        start = i[0]
        end = i[1]
    else:
        #merge the intervals
        end = max(i[1], end)
#storing remaining interval in result
result.append([start,end])
print(result)
        
