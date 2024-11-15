def solution(num, data):
    n = num
    s = data
    T_left = [float('inf')] * n
    T_right = [float('inf')] * n

    # Process right forces
    t = None
    for i in range(n):
        if s[i] == 'R':
            t = 0
            T_right[i] = t
        elif s[i] == 'L':
            t = None  # Right force stops
        elif t is not None:
            t += 1
            T_right[i] = t

    # Process left forces
    t = None
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            t = 0
            T_left[i] = t
        elif s[i] == 'R':
            t = None  # Left force stops
        elif t is not None:
            t += 1
            T_left[i] = t

    # Determine the final state of each domino
    standing_positions = []
    for i in range(n):
        if T_left[i] == T_right[i]:
            # Remains standing if both times are equal
            if T_left[i] == float('inf'):
                # No forces reach this domino
                standing_positions.append(i + 1)  # Positions are 1-based
            else:
                # Forces cancel out
                standing_positions.append(i + 1)
        elif T_left[i] == float('inf') and T_right[i] == float('inf'):
            # No forces reach this domino
            standing_positions.append(i + 1)
        # Else, the domino falls in the direction of the earlier force

    # Format the output
    if standing_positions:
        result = f"{len(standing_positions)}:{','.join(map(str, standing_positions))}"
    else:
        result = "0"
    return result

if __name__ == "__main__":
    # Test cases
    print(solution(14, ".L.R...LR..L..") == "4:3,6,13,14")
    print(solution(5, "R....") == "0")
    print(solution(1, ".") == "1:1")
