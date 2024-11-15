def solution(inputArray):
    # Sort the intervals by start value
    intervals = sorted(inputArray, key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged:
            merged.append(interval)
        else:
            last = merged[-1]
            # Check for overlap; since intervals are [start, end), overlap occurs if current start < last end
            if interval[0] < last[1]:
                # Merge the intervals
                last[1] = max(last[1], interval[1])
            else:
                # No overlap; append the interval
                merged.append(interval)
    # Calculate the total number of unique numbers
    total = 0
    for start, end in merged:
        total += end - start
    return total