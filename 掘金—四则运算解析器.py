def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def apply_op(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a // b  # 整数除法


def to_postfix(expression):
    stack = []  # 操作符栈
    output = []  # 后缀表达式（输出队列）

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # 处理数字
            output.append(expression[i])
        elif expression[i] == '(':
            # 左括号入栈
            stack.append(expression[i])
        elif expression[i] == ')':
            # 右括号，弹出直到遇到左括号
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # 弹出左括号
        else:
            # 操作符，考虑优先级
            while stack and precedence(stack[-1]) >= precedence(expression[i]):
                output.append(stack.pop())
            stack.append(expression[i])
        i += 1

    # 剩余的操作符加入输出
    while stack:
        output.append(stack.pop())

    return output


def evaluate_postfix(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            # 数字直接入栈
            stack.append(int(token))
        else:
            # 操作符，弹出两个操作数
            b = stack.pop()
            a = stack.pop()
            result = apply_op(a, b, token)
            stack.append(result)
    return stack[0]


def solution(expression):
    postfix = to_postfix(expression)
    return evaluate_postfix(postfix)


# 测试
if __name__ == "__main__":
    print(solution("1+1") == 2)
    print(solution("3+4*5/(3+2)") == 7)
    print(solution("4+2*5-2/1") == 12)
    print(solution("(1+(4+5+2)-3)+(6+8)") == 23)
