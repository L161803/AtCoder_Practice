import sys

input = sys.stdin.read
data = input().split()
iterator = iter(data)

N = int(next(iterator))
Q = int(next(iterator))

que = []

intervals = []
current_black_count = 0

for _ in range(Q):
    L = int(next(iterator))
    R = int(next(iterator))
        
    new_L, new_R = L, R
    next_intervals = []
        
    idx = 0
    len_intervals = len(intervals)
        
    while idx < len_intervals and intervals[idx][1] < L - 1:
            
        next_intervals.append(intervals[idx])
        idx += 1
            
        
    while idx < len_intervals and intervals[idx][0] <= R + 1:
            
        new_L = min(new_L, intervals[idx][0])
        new_R = max(new_R, intervals[idx][1])
            
        current_black_count -= (intervals[idx][1] - intervals[idx][0] + 1)
        idx += 1
            
        
    next_intervals.append([new_L, new_R])
    current_black_count += (new_R - new_L + 1)
        
    while idx < len_intervals:
        next_intervals.append(intervals[idx])
        idx += 1

    intervals = next_intervals
    print(N-current_black_count)

