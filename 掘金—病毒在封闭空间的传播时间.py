def solution(row_n, column_m, seats, patient):
    import heapq
    from collections import defaultdict

    # Convert patient coordinates to 0-based indexing
    px, py = patient
    if not (0 <= px < row_n and 0 <= py < column_m):
        return 0  # If patient is out of bounds, no infection spread

    # Initialize infection time grid
    inf = float('inf')
    infection_time = [[inf for _ in range(column_m)] for _ in range(row_n)]
    infection_time[px][py] = 0

    # Priority queue for Dijkstra's algorithm: (time, x, y)
    heap = []
    heapq.heappush(heap, (0, px, py))

    # Dictionary to track infection attempts for masked cells
    # Key: (x, y), Value: defaultdict(int) where key is time and value is attempts
    masked_attempts = defaultdict(lambda: defaultdict(int))

    while heap:
        current_time, x, y = heapq.heappop(heap)

        # If we have already found a better way to infect this cell, skip
        if current_time > infection_time[x][y]:
            continue

        # Explore all four adjacent directions
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            # Check bounds
            if not (0 <= nx < row_n and 0 <= ny < column_m):
                continue

            # If the neighbor is unmasked
            if seats[nx][ny] == 0:
                new_time = current_time + 1
                if new_time < infection_time[nx][ny]:
                    infection_time[nx][ny] = new_time
                    heapq.heappush(heap, (new_time, nx, ny))
            else:
                # Neighbor is masked
                attempt_time = current_time + 1
                masked_attempts[(nx, ny)][attempt_time] += 1

                # If this is the second attempt at the same time, infect at attempt_time
                if masked_attempts[(nx, ny)][attempt_time] == 2:
                    if attempt_time < infection_time[nx][ny]:
                        infection_time[nx][ny] = attempt_time
                        heapq.heappush(heap, (attempt_time, nx, ny))

                # If this is the first attempt, schedule infection at attempt_time + 1
                elif masked_attempts[(nx, ny)][attempt_time] == 1:
                    scheduled_time = attempt_time + 1
                    if scheduled_time < infection_time[nx][ny]:
                        infection_time[nx][ny] = scheduled_time
                        heapq.heappush(heap, (scheduled_time, nx, ny))

    # After processing, find the maximum infection time
    max_time = 0
    for row in infection_time:
        for t in row:
            if t == inf:
                continue  # Assuming all cells can be infected
            if t > max_time:
                max_time = t

    return max_time


if __name__ == "__main__":
    # You can add more test cases here
    testSeats1 = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 1]
    ]
    testSeats2 = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 1]
    ]
    testSeats3 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    testSeats4 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    testSeats5 = [
        [1]
    ]

    print(solution(4, 4, testSeats1, [2, 2]) == 6)
    print(solution(4, 4, testSeats2, [2, 5]) == 0)
    print(solution(4, 4, testSeats3, [2, 2]) == 4)
    print(solution(4, 4, testSeats4, [2, 2]) == 6)
    print(solution(1, 1, testSeats5, [0, 0]) == 0)
