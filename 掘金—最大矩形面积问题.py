def solution(n: int, array: list) -> int:
    stack = []
    max_area = 0
    # Append a zero height to ensure all bars are processed
    extended_array = array + [0]

    for i in range(len(extended_array)):
        while stack and extended_array[i] < extended_array[stack[-1]]:
            top_index = stack.pop()
            height = extended_array[top_index]
            # Width is current index i minus index of previous item in stack minus one
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            area = height * width
            if area > max_area:
                max_area = area
        stack.append(i)

    return max_area


if __name__ == "__main__":
    # Add your test cases here

    print(solution(5, [1, 2, 3, 4, 5]) == 9)

