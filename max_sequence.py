def maxSequence(arr):
    max_sum = 0
    start_idx = 0
    end_idx = 1
    
    
    while end_idx < len(arr):
        start_idx = 0
        while start_idx <= end_idx:
            if sum(arr[start_idx:end_idx+1]) > max_sum:
                max_sum = sum(arr[start_idx:end_idx+1])
            start_idx += 1
        end_idx += 1
    return max_sum
    
    